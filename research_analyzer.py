from upsonic import Task, Agent,Canvas
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from stock_anlayzer import market_research, financial_health, risk_assessment
from helper import get_stock_analysis_report
from pydantic import BaseModel


research_analyst_agent = Agent(name="Research Analyst", 
                                system_prompt=" You are given a stock analyst report and you need to analyzer data synthesizer and data aggregator",
                                model="openai/gpt-4o",
                                company_url="https://www.goldmansachs.com/",
                                company_objective="To deliver superior, value to clients by identifying unique investment opportunities through exhaustive fundamental research.",
)


# Get the stock analysis report
stock_analysis_report = get_stock_analysis_report()



class CompanyInvestmentPotential(BaseModel):
    company_name: str
    Potential: str
    Competitive_Advantages: str
    Market_Positioning: str

#wrapper model for multiple companies
class InvestmentAnalysis(BaseModel):
    companies: List[CompanyInvestmentPotential]
    Relative_Valuations: str
    Overall_Investment_Recommendations: str

class CompanyRiskEvaluation(BaseModel):
    company_name: str
    Risk_Factors: str
    Key_Risks: str
    Impact_on_Growth: str
    Management_Capability: str
    Overall_Risk_Assessment: str

class RiskEvaluation(BaseModel):
    companies: List[CompanyRiskEvaluation]
    Overall_Risk_Assessment: str


#stock_analysis_report is added because it is tested like this and in this way that it provides more accurate results rather than just using the context.
investment_analysis = Task(    
    """Based on the provided stock analysis report focusing on market research and financial health, conduct a comprehensive investment analysis for each company. 
    For each company provided in the stock analysis report, provide:
    1. Investment Potential: Evaluate the company's growth prospects, financial strength, and market opportunities based on their market research and financial health data.
    2. Competitive Advantages: Identify the company's unique strengths, technological advantages, market position, and competitive moats that give them an edge over the other among the companies provided. Look at the market research and financial health data to identify the competitive advantages.
    3. Market Positioning: Assess how well the company is positioned in their market segment, their brand strength, customer base, and strategic initiatives.
    Additionally, provide a 
    **Relative Valuations** section that compares all companies against each other in terms of investment attractiveness and market positioning.
    Finally, provide """ + get_stock_analysis_report(),
    context=[market_research, financial_health],
    agent=research_analyst_agent,
    response_format=InvestmentAnalysis,
)

risk_evaluation = Task(
    """Based on the provided risk assessment data, conduct a risk evaluation for each company by analyzing:
    1. Extract & Summarize Key Risks: From the risk assessment data for each company, extract the primary market, company-specific, and regulatory risks. Synthesize these points into a brief profile of the main threats.
    2. Analyze Impact on Growth: Evaluate how this combined risk profile impacts each company's growth sustainability. Assess their ability to manage these threats based on the market positioning and advantages provided in the investment analysis. 
    Use the following risk assessment data: """ + get_stock_analysis_report(),
    context=[risk_assessment, investment_analysis],
    agent=research_analyst_agent,
    response_format=RiskEvaluation,
)



research_analyst_agent.print_do(investment_analysis)