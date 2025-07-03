from upsonic import Task, Agent,Canvas
from upsonic.tools import Search
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional
from google_search_mcp import GoogleSearchMCP

load_dotenv()

company_names = ["Oracle","Upsonic","Google","Apple"]

# Pydantic models for individual company data
class CompanyMarketPosition(BaseModel):
    company: str
    market_share: Optional[str] = None
    competitive_position: str
    key_metrics: List[str]
    recent_performance: str

class CompanyFinancialHealth(BaseModel):
    company: str
    financial_ratios: List[str]
    analyst_recommendations: List[str]
    growth_catalysts: List[str]
    earnings_summary: str

class CompanyInvestmentRisk(BaseModel):
    company: str
    market_risks: List[str]
    company_specific_risks: List[str]
    regulatory_risks: List[str]
    overall_risk_level: str  # "Low", "Medium", "High"

# Wrapper models for multiple companies
class MarketPosition(BaseModel):
    companies: List[CompanyMarketPosition]

class FinancialHealth(BaseModel):
    companies: List[CompanyFinancialHealth]

class InvestmentRisk(BaseModel):
    companies: List[CompanyInvestmentRisk]

stock_analysis_canvas = Canvas("Stock Analysis Report")

stock_analyst_agent = Agent(name="Stock Analyst", 
              system_prompt="You are given a list of companies and you need to analyze the companies based on recent news and reports as a stock analyst. The alaysis should include numeric datas from the latest news and reports. Edit canvas after each task is completed.",
              model="openai/gpt-4o",
              #Focused on the research objective of Goldman Sachs
              company_url="https://www.goldmansachs.com/",
              company_objective="To deliver superior, long-term value to clients by identifying unique investment opportunities through exhaustive fundamental research.",
              canvas=stock_analysis_canvas
              )


market_research = Task(
    "Analyze each given company's market position, key performance metrics, and competitive landscape using Google search to find the latest financial data, market share information, and competitive analysis." + "Companies: " + str(company_names),  
    context=[company_names],
    tools=[GoogleSearchMCP],
    response_format=MarketPosition,
    agent=stock_analyst_agent
)

financial_health = Task(
    "Evaluate each company's financial health by searching for key financial ratios, analyst recommendations, earnings reports, and recent news to identify primary growth catalysts." + "Companies: " + str(company_names),
    context=[company_names],
    tools=[GoogleSearchMCP],
    response_format=FinancialHealth,
    agent=stock_analyst_agent
)

risk_assessment = Task(
    "Identify and summarize all significant investment risks by searching for market analysis, company-specific risks, regulatory issues, and macroeconomic factors that could impact these companies." + "Companies: " + str(company_names),
    context=[company_names],
    tools=[GoogleSearchMCP],
    response_format=InvestmentRisk,
    agent=stock_analyst_agent
)




#Save the response to a file as text

stock_analyst_agent.print_do(market_research)
market_research_response = market_research.response

with open("market_research_response.txt", "w") as f:
    f.write(str(market_research_response))

stock_analyst_agent.print_do(financial_health)
financial_health_response = financial_health.response

with open("financial_health_response.txt", "w") as f:
    f.write(str(financial_health_response))

stock_analyst_agent.print_do(risk_assessment)
risk_assessment_response = risk_assessment.response

with open("risk_assessment_response.txt", "w") as f:
    f.write(str(risk_assessment_response))