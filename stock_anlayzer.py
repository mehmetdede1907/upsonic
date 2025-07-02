import os
from upsonic import Task, Agent
from upsonic.tools import Search
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

company_names = ["Oracle","Upsonic","Google","Apple"]

# MCP Tools - Using only working MCP servers
class FetchMCP:
    command = "uvx"
    args = ["mcp-server-fetch"]

market_research = Task(
    "Analyze each given company's market position, key performance metrics, and competitive landscape using web search to find the latest financial data, market share information, and competitive analysis." + str(company_names),  
    tools=[FetchMCP, Search],
)

financial_health = Task(
    "Evaluate each company's financial health by searching for key financial ratios, analyst recommendations, earnings reports, and recent news to identify primary growth catalysts." + str(company_names),
    tools=[FetchMCP, Search],
)

risk_assessment = Task(
    "Identify and summarize all significant investment risks by searching for market analysis, company-specific risks, regulatory issues, and macroeconomic factors that could impact these companies." + str(company_names),
    tools=[FetchMCP, Search],
)

agent = Agent(name="Stock Analyst", model="openai/gpt-4o")

agent.print_do(market_research)
agent.print_do(financial_health)
agent.print_do(risk_assessment)

