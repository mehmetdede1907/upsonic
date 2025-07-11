# test.py

import time
from upsonic.utils.package.exception import AgentExecutionError

from agents.stock_anlayzer import stock_analyst_agent
from agents.research_analyzer import research_analyst_agent
from agents.investment_lead import investment_lead_agent

from tasks.stock_anlaysis_tasks import market_research, financial_health, risk_assessment
from tasks.research_anlaysis_tasks import investment_analysis, risk_evaluation
from tasks.investment_lead_tasks import (
    develop_portfolio_strategy,
    articulate_investment_rationale,
    prepare_final_recommendation
)

from utils.file_handler import (
    save_stock_analysis_report,
    save_research_analysis_report,
    save_investment_lead_analysis_report
)

def run_task_with_retry(agent, task, max_retries=3, delay=15):
    """
    Runs a task with a given agent, retrying on failure.
    
    Args:
        agent: The agent to execute the task.
        task: The task to be executed.
        max_retries (int): Maximum number of retries.
        delay (int): Seconds to wait between retries.
    """
    for attempt in range(max_retries):
        try:
            print(f"Executing task '{task.description[:50]}...' (Attempt {attempt + 1}/{max_retries})")
            agent.print_do(task)
            print(f"Task '{task.description[:50]}...' completed successfully.")
            return # Exit the function on success
        except AgentExecutionError as e:
            print(f"Error during agent execution: {e}")
            if attempt < max_retries - 1:
                print(f"Model may be overloaded. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max retries reached. Moving on to the next task.")
                # We can choose to raise the exception here to stop the script,
                # but for this flow, we'll just log it and continue.
                # raise e 

def run_tests():
    """
    Runs each task individually with its agent for testing and visualization,
    including a retry mechanism for transient errors.
    """
    print("--- Running Tier 1: Stock Analyst ---")
    run_task_with_retry(stock_analyst_agent, market_research)
    run_task_with_retry(stock_analyst_agent, financial_health)
    run_task_with_retry(stock_analyst_agent, risk_assessment)
    save_stock_analysis_report(market_research, financial_health, risk_assessment)
    print("\n--- Stock Analysis Report Saved ---\n")

    print("--- Running Tier 2: Research Analyst ---")
    run_task_with_retry(research_analyst_agent, investment_analysis)
    run_task_with_retry(research_analyst_agent, risk_evaluation)
    save_research_analysis_report(investment_analysis, risk_evaluation)
    print("\n--- Research Analysis Report Saved ---\n")

    print("--- Running Tier 3: Investment Lead ---")
    run_task_with_retry(investment_lead_agent, develop_portfolio_strategy)
    run_task_with_retry(investment_lead_agent, articulate_investment_rationale)
    run_task_with_retry(investment_lead_agent, prepare_final_recommendation)
    save_investment_lead_analysis_report(
        develop_portfolio_strategy,
        articulate_investment_rationale,
        prepare_final_recommendation
    )
    print("\n--- Investment Lead Report Saved ---\n")
    
    print("All test tasks completed and reports saved in the 'reports/' directory.")

if __name__ == "__main__":
    run_tests()