import os
from upsonic import Task, Agent
from upsonic.tools import Search
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

company_names = ["Oracle","Upsonic","Google","Apple"]
# company_urls = ["https://www.oracle.com/","https://upsonic.ai/","https://www.google.com/","https://www.apple.com/"]
# class FetchMCP:
#     command = "uvx"
#     args = ["mcp-server-fetch"]

class GoogleSearchMCP:
    command = "node"
    args = [os.path.join(os.getcwd(), "google-search-mcp", "dist", "index.js")]
    env = {
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY", ""),
        "GOOGLE_CSE_ID": os.getenv("GOOGLE_CSE_ID", "")
    }

market_research = Task(
    "Analyze each given company's market position, key performance metrics, and competitive landscape using Google search to find the latest financial data, market share information, and competitive analysis." + str(company_names),  
    tools=[GoogleSearchMCP,Search],
)

financial_health = Task(
    "Evaluate each company's financial health by searching for key financial ratios, analyst recommendations, earnings reports, and recent news to identify primary growth catalysts." + str(company_names),
    tools=[GoogleSearchMCP,Search],
)

risk_assessment = Task(
    "Identify and summarize all significant investment risks by searching for market analysis, company-specific risks, regulatory issues, and macroeconomic factors that could impact these companies." + str(company_names),
    tools=[GoogleSearchMCP,Search],
)

agent = Agent(name="Stock Analyst", system_prompt="You are given a list of companies and you need to analyze their market position, financial health, and investment risks the alaysis should include numeric datas from the latest news and reports.", model="openai/gpt-4o")

agent.print_do(market_research)
agent.print_do(financial_health)
agent.print_do(risk_assessment)

