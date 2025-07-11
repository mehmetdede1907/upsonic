# tasks/research_analysis_tasks.py

from upsonic import Task
from pydantic import BaseModel
from typing import List
from agents.research_analyzer import research_analyst_agent

class CompanyInvestmentPotential(BaseModel):
    company_name: str
    potential: str
    competitive_advantages: str
    market_positioning: str

class InvestmentAnalysis(BaseModel):
    companies: List[CompanyInvestmentPotential]
    relative_valuations: str
    overall_investment_recommendations: str

class CompanyRiskEvaluation(BaseModel):
    company_name: str
    risk_factors: str
    key_risks: str
    impact_on_growth: str
    management_capability: str
    overall_risk_assessment: str

class RiskEvaluation(BaseModel):
    companies: List[CompanyRiskEvaluation]
    overall_risk_assessment: str

def create_research_analysis_tasks(market_research, financial_health, risk_assessment):
    """
    Creates research analysis tasks based on the provided stock analysis tasks.
    """
    investment_analysis = Task(
        "Based on the provided market research and financial health, conduct a comprehensive investment analysis for each company.",
        context=[market_research, financial_health],
        agent=research_analyst_agent,
        response_format=InvestmentAnalysis,
    )

    risk_evaluation = Task(
        "Based on the provided risk assessment data, conduct a detailed risk evaluation for each company.",
        context=[risk_assessment, investment_analysis],
        agent=research_analyst_agent,
        response_format=RiskEvaluation,
    )
    
    return investment_analysis, risk_evaluation

# Create default tasks using the default stock analysis tasks
from .stock_anlaysis_tasks import market_research, financial_health, risk_assessment

investment_analysis, risk_evaluation = create_research_analysis_tasks(market_research, financial_health, risk_assessment)