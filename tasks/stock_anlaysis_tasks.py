# tasks/stock_analysis_tasks.py

from upsonic import Task
from pydantic import BaseModel
from typing import List, Optional
import os
from agents.stock_anlayzer import stock_analyst_agent

class GoogleSearchMCP:
    command = "node"
    args = [os.path.join(os.getcwd(), "google-search-mcp", "dist", "index.js")]
    env = {
        "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY", ""),
        "GOOGLE_CSE_ID": os.getenv("GOOGLE_CSE_ID", "")
    }

class CompanyMarketPosition(BaseModel):
    company: str
    market_share: Optional[str] = None
    competitive_position: str
    key_metrics: List[str]
    recent_performance: str

class MarketPosition(BaseModel):
    companies: List[CompanyMarketPosition]

class CompanyFinancialHealth(BaseModel):
    company: str
    financial_ratios: List[str]
    analyst_recommendations: List[str]
    growth_catalysts: List[str]
    earnings_summary: str

class FinancialHealth(BaseModel):
    companies: List[CompanyFinancialHealth]

class CompanyInvestmentRisk(BaseModel):
    company: str
    market_risks: List[str]
    company_specific_risks: List[str]
    regulatory_risks: List[str]
    current_risks: List[str]
    overall_risk_level: str

class InvestmentRisk(BaseModel):
    companies: List[CompanyInvestmentRisk]

from config import COMPANY_NAMES

def create_stock_analysis_tasks(company_names: List[str]):
    companies_str = ", ".join(company_names)

    market_research = Task(
        f"Analyze each given company's market position, key performance metrics, and competitive landscape. Companies: {companies_str}",
        tools=[GoogleSearchMCP],
        response_format=MarketPosition,
        agent=stock_analyst_agent,
    )

    financial_health_task = Task(
        f"Evaluate each company's financial health, including key ratios, analyst ratings, and growth catalysts. Companies: {companies_str}",
        tools=[GoogleSearchMCP],
        response_format=FinancialHealth,
        agent=stock_analyst_agent,
    )

    risk_assessment_task = Task(
        f"Identify and summarize significant investment risks for each company. Companies: {companies_str}",
        tools=[GoogleSearchMCP],
        response_format=InvestmentRisk,
        agent=stock_analyst_agent
    )
    
    return market_research, financial_health_task, risk_assessment_task

# Create default tasks at module level
companies_str = ", ".join(COMPANY_NAMES)

market_research = Task(
    f"Analyze each given company's market position, key performance metrics, and competitive landscape. Companies: {companies_str}",
    tools=[GoogleSearchMCP],
    response_format=MarketPosition,
    agent=stock_analyst_agent,
)

financial_health = Task(
    f"Evaluate each company's financial health, including key ratios, analyst ratings, and growth catalysts. Companies: {companies_str}",
    tools=[GoogleSearchMCP],
    response_format=FinancialHealth,
    agent=stock_analyst_agent,
)

risk_assessment = Task(
    f"Identify and summarize significant investment risks for each company. Companies: {companies_str}",
    tools=[GoogleSearchMCP],
    response_format=InvestmentRisk,
    agent=stock_analyst_agent
)