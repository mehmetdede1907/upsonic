from upsonic import Task, Agent,Canvas
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from .research_analyzer import investment_analysis, risk_evaluation


load_dotenv()

class CompanyPortfolioStrategy(BaseModel):
    company_name: str
    percentage_allocation: float
    investment_timeframe: str

class PortfolioStrategy(BaseModel):
    companies: List[CompanyPortfolioStrategy]

class CompanyInvestmentRationale(BaseModel):
    company_name: str
    investment_rationale: str

class InvestmentRationale(BaseModel):
    companies: List[CompanyInvestmentRationale]

class FinalRecommendation(BaseModel):
    portfolio_strategy: PortfolioStrategy
    investment_rationale: InvestmentRationale
    overall_recommendation: str

investment_lead_agent = Agent(
    name="Investment Lead",
    model="openai/gpt-4o",
    company_url="https://www.goldmansachs.com/",
    company_objective="To deliver superior, value to clients by identifying unique investment opportunities through exhaustive fundamental research.",
)

develop_portfolio_strategy = Task(
    description="Based on the final investment analysis, develop a strategic portfolio allocation. Define the percentage allocation for each recommended company, ensuring the portfolio is optimized for a balanced risk-reward profile and proper diversification. Specify the recommended investment timeframe (e.g., Short-term, Medium-term, Long-term).",
    context=[investment_analysis, risk_evaluation], 
    agent=investment_lead_agent,
    response_format=PortfolioStrategy,
)

articulate_investment_rationale = Task(
    description="For the defined portfolio strategy, articulate a clear and compelling investment rationale. Explain the reasoning behind each allocation decision, supporting it with key findings from the previous analysis. Proactively address potential concerns and re-emphasize the primary growth catalysts that justify the investment.",
    context=[develop_portfolio_strategy, investment_analysis, risk_evaluation], # Requires the output of the portfolio strategy task 
    agent=investment_lead_agent,
    response_format=InvestmentRationale,

)

prepare_final_recommendation = Task(
    description="Compile a final, client-ready investment recommendation report. Present the portfolio with clear percentage allocations in a table. Summarize the core investment thesis and provide actionable next steps for the investor. Conclude with a clear summary of the key risks associated with the overall portfolio. Mention the reasson for each allocation decision concisely.",
    context=[develop_portfolio_strategy, articulate_investment_rationale], # Requires the output of the rationale task
    agent=investment_lead_agent,
    response_format=FinalRecommendation,
)







