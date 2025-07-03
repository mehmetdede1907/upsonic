from upsonic import Task, Agent, Canvas, Team
from stock_anlayzer import market_research, financial_health, risk_assessment, stock_analyst_agent
from helper import save_stock_analysis_report, save_research_analysis_report, save_investment_lead_analysis_report
from research_analyzer import investment_analysis, risk_evaluation, research_analyst_agent
from investment_lead import develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation, investment_lead_agent



# Create Canvas for Stock Analysis
team = Team(
    agents=[stock_analyst_agent, research_analyst_agent, investment_lead_agent],
    tasks=[market_research, financial_health, risk_assessment, investment_analysis, risk_evaluation, develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation]
)
team.complete()



# stock_analyst_agent.print_do(market_research)

# stock_analyst_agent.print_do(financial_health)

# stock_analyst_agent.print_do(risk_assessment)

# #Save the response to a file as proper format
# save_stock_analysis_report(market_research, financial_health, risk_assessment)

# research_analyst_agent.print_do(investment_analysis)

# research_analyst_agent.print_do(risk_evaluation)

# # Save the research analysis responses to a file as proper format
# save_research_analysis_report(investment_analysis, risk_evaluation)

# investment_lead_agent.print_do(develop_portfolio_strategy)

# investment_lead_agent.print_do(articulate_investment_rationale)

# investment_lead_agent.print_do(prepare_final_recommendation)

# save_investment_lead_analysis_report(develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation)










