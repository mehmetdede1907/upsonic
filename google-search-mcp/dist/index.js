import dotenv from "dotenv";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema, } from "@modelcontextprotocol/sdk/types.js";
dotenv.config();
// Define the web search tool
const WEB_SEARCH_TOOL = {
    name: "google_web_search",
    description: "Performs a web search using Google's Custom Search API to find current information and news.",
    inputSchema: {
        type: "object",
        properties: {
            query: {
                type: "string",
                description: "The search query to perform",
            },
            count: {
                type: "number",
                description: "Number of results to return (1-10, default 5)",
                default: 5,
            },
            start: {
                type: "number",
                description: "Pagination start index (default 1)",
                default: 1,
            },
            site: {
                type: "string",
                description: "Limit search to specific site (e.g., 'example.com')",
            },
        },
        required: ["query"],
    },
};
// Check for API key and Search Engine ID
const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;
const GOOGLE_CSE_ID = process.env.GOOGLE_CSE_ID;
if (!GOOGLE_API_KEY || !GOOGLE_CSE_ID) {
    console.error("Error: Missing environment variables GOOGLE_API_KEY or GOOGLE_CSE_ID");
    process.exit(1);
}
// Create the server
const server = new Server({
    name: "google-search",
    version: "0.1.0",
}, {
    capabilities: {
        tools: {},
    },
});
// Handle tool listing
server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [WEB_SEARCH_TOOL],
}));
// Handle tool calls
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    if (name === "google_web_search") {
        try {
            const { query, count = 5, start = 1, site } = args;
            // Build the Google Custom Search API URL
            let url = `https://www.googleapis.com/customsearch/v1?key=${GOOGLE_API_KEY}&cx=${GOOGLE_CSE_ID}&q=${encodeURIComponent(query)}&num=${Math.min(count, 10)}&start=${start}`;
            if (site) {
                url += `&siteSearch=${encodeURIComponent(site)}`;
            }
            // Make the API request
            const response = await fetch(url);
            const data = await response.json();
            if (!response.ok) {
                throw new Error(`Google API error: ${data.error?.message || 'Unknown error'}`);
            }
            // Format the results
            const results = data.items?.map((item) => ({
                title: item.title,
                url: item.link,
                description: item.snippet,
                metadata: {
                    type: "web_result",
                    source: new URL(item.link).hostname,
                },
            })) || [];
            return {
                content: [
                    {
                        type: "text",
                        text: JSON.stringify({
                            type: "search_results",
                            data: results,
                            metadata: {
                                query,
                                resultCount: results.length,
                                totalResults: data.searchInformation?.totalResults || 0,
                            },
                        }, null, 2),
                    },
                ],
            };
        }
        catch (error) {
            return {
                content: [
                    {
                        type: "text",
                        text: `Error performing web search: ${error instanceof Error ? error.message : 'Unknown error'}`,
                    },
                ],
                isError: true,
            };
        }
    }
    throw new Error(`Unknown tool: ${name}`);
});
// Run the server
async function runServer() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.error("Google Search MCP Server running on stdio");
}
runServer().catch((error) => {
    console.error("Fatal error running server:", error);
    process.exit(1);
});
