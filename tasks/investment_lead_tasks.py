# tasks/investment_lead_tasks.py

from upsonic import Task
from pydantic import BaseModel
from typing import List
from agents.investment_lead import investment_lead_agent
from .research_anlaysis_tasks import investment_analysis, risk_evaluation

class CompanyPortfolioStrategy(BaseModel):
    company_name: str
    percentage_allocation: float
    investment_timeframe: str

class PortfolioStrategy(BaseModel):
    companies: List[CompanyPortfolioStrategy]

develop_portfolio_strategy = Task(
    "Develop a strategic portfolio allocation based on the investment analysis and risk evaluation.",
    context=[investment_analysis, risk_evaluation],
    agent=investment_lead_agent,
    response_format=PortfolioStrategy,
)

class CompanyInvestmentRationale(BaseModel):
    company_name: str
    investment_rationale: str

class InvestmentRationale(BaseModel):
    companies: List[CompanyInvestmentRationale]

articulate_investment_rationale = Task(
    "Articulate a clear investment rationale for the defined portfolio strategy.",
    context=[develop_portfolio_strategy, investment_analysis, risk_evaluation],
    agent=investment_lead_agent,
    response_format=InvestmentRationale,
)

class FinalRecommendation(BaseModel):
    portfolio_strategy: PortfolioStrategy
    investment_rationale: InvestmentRationale
    overall_recommendation: str

prepare_final_recommendation = Task(
    "Compile a final, client-ready investment recommendation report.",
    context=[develop_portfolio_strategy, articulate_investment_rationale],
    agent=investment_lead_agent,
    response_format=FinalRecommendation,
)