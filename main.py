from upsonic import Task, Agent, Canvas, Team
from stock_anlayzer import market_research, financial_health, risk_assessment, stock_analyst_agent, set_company_names
from helper import save_stock_analysis_report, save_research_analysis_report, save_investment_lead_analysis_report
from research_analyzer import investment_analysis, risk_evaluation, research_analyst_agent
from investment_lead import develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation, investment_lead_agent

# Get company names from user input
user_input = input("Enter the company ticker symbols separated by commas: ")
company_names = [name.strip().upper() for name in user_input.split(",") if name.strip()]

# Set the global company names variable
set_company_names(company_names)

# Create Canvas for Stock Analysis
team = Team(
    agents=[stock_analyst_agent, research_analyst_agent, investment_lead_agent],
    tasks=[market_research, financial_health, risk_assessment, investment_analysis, risk_evaluation, develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation]
)
team.complete()











