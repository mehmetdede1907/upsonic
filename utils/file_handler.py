# utils/file_handler.py

import json
import os

REPORTS_DIR = "reports"

def save_report(data, filename):
    """
    Saves data to a JSON file in the reports directory.
    """
    os.makedirs(REPORTS_DIR, exist_ok=True)
    filepath = os.path.join(REPORTS_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Report saved to {filepath}")

def save_stock_analysis_report(market_research, financial_health, risk_assessment):
    report = {
        "market_research": market_research.response.model_dump() if hasattr(market_research, 'response') and market_research.response else "No response available",
        "financial_health": financial_health.response.model_dump() if hasattr(financial_health, 'response') and financial_health.response else "No response available",
        "risk_assessment": risk_assessment.response.model_dump() if hasattr(risk_assessment, 'response') and risk_assessment.response else "No response available",
    }
    save_report(report, "stock_analysis_report.json")

def get_stock_analysis_report():
    try:
        with open(os.path.join(REPORTS_DIR, "stock_analysis_report.json"), 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Warning: Could not read stock analysis report: {e}")
        return {}

def save_research_analysis_report(investment_analysis, risk_evaluation):
    report = {
        "investment_analysis": investment_analysis.response.model_dump() if hasattr(investment_analysis, 'response') and investment_analysis.response else "No response available",
        "risk_evaluation": risk_evaluation.response.model_dump() if hasattr(risk_evaluation, 'response') and risk_evaluation.response else "No response available",
    }
    save_report(report, "research_analysis_report.json")

def save_investment_lead_analysis_report(develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation):
    report = {
        "portfolio_strategy": develop_portfolio_strategy.response.model_dump() if hasattr(develop_portfolio_strategy, 'response') and develop_portfolio_strategy.response else "No response available",
        "investment_rationale": articulate_investment_rationale.response.model_dump() if hasattr(articulate_investment_rationale, 'response') and articulate_investment_rationale.response else "No response available",
        "final_recommendation": prepare_final_recommendation.response.model_dump() if hasattr(prepare_final_recommendation, 'response') and prepare_final_recommendation.response else "No response available",
    }
    save_report(report, "investment_lead_analysis_report.json")