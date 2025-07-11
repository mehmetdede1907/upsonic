# main.py

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn
import time
import os

# Import agents
from agents.stock_anlayzer import stock_analyst_agent
from agents.research_analyzer import research_analyst_agent
from agents.investment_lead import investment_lead_agent

# Import tasks
from tasks.stock_anlaysis_tasks import market_research, financial_health, risk_assessment
from tasks.research_anlaysis_tasks import investment_analysis, risk_evaluation
from tasks.investment_lead_tasks import develop_portfolio_strategy, articulate_investment_rationale, prepare_final_recommendation

# Import utility functions
from upsonic.utils.package.exception import AgentExecutionError
from utils.file_handler import (
    save_stock_analysis_report,
    save_research_analysis_report,
    save_investment_lead_analysis_report
)

app = FastAPI(title="Stock Analysis API", description="AI-Powered Stock Analysis and Investment Recommendations")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (frontend)
if os.path.exists("frontend"):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")

class AnalysisRequest(BaseModel):
    tickers: List[str]

def run_task_with_retry(agent, task, max_retries=3, delay=15):
    for attempt in range(max_retries):
        try:
            print(f"Executing task '{task.description[:50]}...' (Attempt {attempt + 1}/{max_retries})")
            agent.print_do(task)
            print(f"Task '{task.description[:50]}...' completed successfully.")
            return
        except AgentExecutionError as e:
            print(f"Error during agent execution: {e}")
            if attempt < max_retries - 1:
                print(f"Model may be overloaded. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max retries reached. Failing task.")
                raise e

@app.post("/run-full-analysis/")
async def run_full_analysis(request: AnalysisRequest):
    try:
        tickers = request.tickers
        if not tickers:
            raise HTTPException(status_code=400, detail="Ticker list cannot be empty.")

        # --- Tier 1: Stock Analyst ---
        run_task_with_retry(stock_analyst_agent, market_research)
        run_task_with_retry(stock_analyst_agent, financial_health)
        run_task_with_retry(stock_analyst_agent, risk_assessment)
        save_stock_analysis_report(market_research, financial_health, risk_assessment)
        print("\n--- Stock Analysis Report Saved ---\n")

        # --- Tier 2: Research Analyst ---
        run_task_with_retry(research_analyst_agent, investment_analysis)
        run_task_with_retry(research_analyst_agent, risk_evaluation)
        save_research_analysis_report(investment_analysis, risk_evaluation)
        print("\n--- Research Analysis Report Saved ---\n")

        # --- Tier 3: Investment Lead ---
        run_task_with_retry(investment_lead_agent, develop_portfolio_strategy)
        run_task_with_retry(investment_lead_agent, articulate_investment_rationale)
        run_task_with_retry(investment_lead_agent, prepare_final_recommendation)
        save_investment_lead_analysis_report(
            develop_portfolio_strategy,
            articulate_investment_rationale,
            prepare_final_recommendation
        )
        print("\n--- Investment Lead Report Saved ---\n")

        return {"message": f"Full analysis completed for {', '.join(tickers)}."}

    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def serve_frontend():
    """Serve the frontend application"""
    if os.path.exists("frontend/index.html"):
        return FileResponse("frontend/index.html")
    else:
        return {"message": "Frontend not found. Please ensure the frontend directory exists."}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Stock Analysis API"}

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)