from upsonic import Task, Agent, Canvas
from stock_anlayzer import market_research, financial_health, risk_assessment, stock_analyst_agent
import json

# Create Canvas for Stock Analysis

stock_analyst_agent.print_do(market_research)

stock_analyst_agent.print_do(financial_health)

stock_analyst_agent.print_do(risk_assessment)

#Save the response to a file as proper format

with open("stock_analysis_structured_report.md", "w") as f:
    f.write("# Stock Analysis Structured Report\n\n")
    f.write("## Market Research\n")
    f.write("```json\n")
    f.write(json.dumps(market_research.response.model_dump(), indent=2) if hasattr(market_research, 'response') and market_research.response else "No response available")
    f.write("\n```\n\n")
    f.write("## Financial Health\n")
    f.write("```json\n")
    f.write(json.dumps(financial_health.response.model_dump(), indent=2) if hasattr(financial_health, 'response') and financial_health.response else "No response available")
    f.write("\n```\n\n")
    f.write("## Risk Assessment\n")
    f.write("```json\n")
    f.write(json.dumps(risk_assessment.response.model_dump(), indent=2) if hasattr(risk_assessment, 'response') and risk_assessment.response else "No response available")
    f.write("\n```\n")








