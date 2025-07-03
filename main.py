from upsonic import Task, Agent, Canvas
from stock_anlayzer import market_research, financial_health, risk_assessment, stock_analyst_agent
from helper import save_stock_analysis_report, save_research_analysis_report
from research_analyzer import investment_analysis, risk_evaluation, research_analyst_agent

# Create Canvas for Stock Analysis

stock_analyst_agent.print_do(market_research)

stock_analyst_agent.print_do(financial_health)

stock_analyst_agent.print_do(risk_assessment)

#Save the response to a file as proper format
save_stock_analysis_report(market_research, financial_health, risk_assessment)

research_analyst_agent.print_do(investment_analysis)

research_analyst_agent.print_do(risk_evaluation)

# Save the research analysis responses to a file as proper format
save_research_analysis_report(investment_analysis, risk_evaluation)









