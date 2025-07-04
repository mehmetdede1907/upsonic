from upsonic import Task, Agent,Canvas
from upsonic.tools import Search
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List, Optional
from google_search_mcp import GoogleSearchMCP

load_dotenv()

company_names = ["AAPL", "GOOG", "ORCL"]

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
    current_risks: List[str]
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
              system_prompt="You are given a list of companies and you need to analyze the companies based on recent news and reports as a stock analyst. The alaysis should include numeric datas from the latest news and reports. Put the exact tasks results in the canvas after each task is completed without changing task output.",
              model="openai/gpt-4o",
              #Focused on the research objective of Goldman Sachs
              company_url="https://www.goldmansachs.com/",
              company_objective="To deliver superior, long-term value to clients by identifying unique investment opportunities through exhaustive fundamental research.",
              canvas=stock_analysis_canvas
              )


market_research = Task(
    "Analyze each given company's market position, key performance metrics, and competitive landscape using Google search. Analyze recent news and reports to provide the recent performance of the company." + "Companies: " + str(company_names),  
    context=[company_names],
    tools=[GoogleSearchMCP],
    response_format=MarketPosition,
    agent=stock_analyst_agent,
)

financial_health = Task(
    """Evaluate each company's financial health by searching for the followings:
    1. Key financial ratios, 
    2. Analyst recommendations by looking at ratings and price targets from recent analysis, 
    3. Earnings reports by looking at the latest data and analyst reports, 
    4. Growth catalysts by looking at the latest news and reports.
    Include numeric data from the latest news and reports.
    Companies: """ + str(company_names),
    context=[company_names],
    tools=[GoogleSearchMCP],
    response_format=FinancialHealth,
    agent=stock_analyst_agent,
)

risk_assessment = Task(
    """Identify and summarize all significant investment risks by searching for the followings:
    1. Market risks like industry trends, macroeconomic factors, market volatility, competitive threats
    2. Company-specific risks mainly internal risks like management issues, operational challenges, financial weaknesses
    3. Regulatory issues like government regulations, compliance issues, legal challenges, antitrust concerns
    4. Current risks from recent news and reports.
    Include numeric data from the latest news and reports.
    Companies: """ + str(company_names),
    context=[company_names],
    tools=[GoogleSearchMCP],
    response_format=InvestmentRisk,
    agent=stock_analyst_agent
)

def set_company_names(names):
    """Set the global company names variable"""
    global company_names
    company_names = names