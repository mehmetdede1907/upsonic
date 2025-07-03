import json

def save_stock_analysis_report(market_research, financial_health, risk_assessment, filename="stock_analysis_structured_report.md"):
    """
    Save stock analysis results to a structured markdown file.
    
    Args:
        market_research: Market research task result
        financial_health: Financial health task result
        risk_assessment: Risk assessment task result
        filename: Output filename (default: stock_analysis_structured_report.md)
    """
    with open(filename, "w") as f:
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
    
    print(f"Stock analysis report saved to {filename}")

def get_stock_analysis_report(filename="stock_analysis_structured_report.md"):
    """
    Read stock analysis report from file and return as string.
    
    Args:
        filename: Input filename (default: stock_analysis_structured_report.md)
        
    Returns:
        str: Content of the stock analysis report
    """
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Returning empty string.")
        return ""
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return ""

def save_research_analysis_report(investment_analysis, risk_evaluation, filename="research_analysis_report.md"):
    """
    Save research analysis results to a structured markdown file.
    
    Args:
        investment_analysis: Investment analysis task result
        risk_evaluation: Risk evaluation task result
        filename: Output filename (default: research_analysis_report.md)
    """
    with open(filename, "w") as f:
        f.write("# Research Analysis Report\n\n")
        
        f.write("## Investment Analysis\n")
        f.write("```json\n")
        f.write(json.dumps(investment_analysis.response.model_dump(), indent=2) if hasattr(investment_analysis, 'response') and investment_analysis.response else "No response available")
        f.write("\n```\n\n")
        
        f.write("## Risk Evaluation\n")
        f.write("```json\n")
        f.write(json.dumps(risk_evaluation.response.model_dump(), indent=2) if hasattr(risk_evaluation, 'response') and risk_evaluation.response else "No response available")
        f.write("\n```\n")
    
    print(f"Research analysis report saved to {filename}") 

def save_investment_lead_analysis_report(develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation, filename="investment_lead_analysis_report.md"):
    """
    Save investment lead analysis results to a structured markdown file.
    
    Args:
        develop_portfolio_strategy: Portfolio strategy task result
        articulate_investment_rationale: Investment rationale task result
        prepare_final_recommendation: Final recommendation task result
        filename: Output filename (default: investment_lead_analysis_report.md)
    """
    with open(filename, "w") as f:
        f.write("# Investment Lead Analysis Report\n\n")
        
        f.write("## Portfolio Strategy\n")
        f.write("```json\n")
        f.write(json.dumps(develop_portfolio_strategy.response.model_dump(), indent=2) if hasattr(develop_portfolio_strategy, 'response') and develop_portfolio_strategy.response else "No response available")
        f.write("\n```\n\n")
        
        f.write("## Investment Rationale\n")
        f.write("```json\n")
        f.write(json.dumps(articulate_investment_rationale.response.model_dump(), indent=2) if hasattr(articulate_investment_rationale, 'response') and articulate_investment_rationale.response else "No response available")
        f.write("\n```\n\n")
        
        f.write("## Final Recommendation\n")
        f.write("```json\n")
        f.write(json.dumps(prepare_final_recommendation.response.model_dump(), indent=2) if hasattr(prepare_final_recommendation, 'response') and prepare_final_recommendation.response else "No response available")
        f.write("\n```\n")