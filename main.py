# main.py

from upsonic import Team
from agents.stock_anlayzer import stock_analyst_agent
from agents.research_analyzer import research_analyst_agent
from agents.investment_lead import investment_lead_agent
from tasks.stock_anlaysis_tasks import market_research, financial_health, risk_assessment
from tasks.research_anlaysis_tasks import investment_analysis, risk_evaluation
from tasks.investment_lead_tasks import develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation
from utils.file_handler import (
    save_stock_analysis_report,
    save_research_analysis_report,
    save_investment_lead_analysis_report,
)

def main():
    """
    Main function to run the AI Stock Analysis System.
    """
    # Define the team of agents
    investment_team = Team(
        agents=[stock_analyst_agent, research_analyst_agent, investment_lead_agent],
        tasks=[
            market_research,
            financial_health,
            risk_assessment,
            investment_analysis,
            risk_evaluation,
            develop_portfolio_strategy,
            articulate_investment_rationale,
            prepare_final_recommendation,
        ]
    )

    # Execute the tasks
    investment_team.complete()

    # Save the final reports
    print("Saving reports...")
    save_stock_analysis_report(market_research, financial_health, risk_assessment)
    save_research_analysis_report(investment_analysis, risk_evaluation)
    save_investment_lead_analysis_report(
        develop_portfolio_strategy,
        articulate_investment_rationale,
        prepare_final_recommendation,
    )
    print("All reports have been saved in the 'reports/' directory.")

if __name__ == "__main__":
    main()