# agents/stock_analyzer_agent.py

from upsonic import Agent
import os

stock_analyst_agent = Agent(
    name="Stock Analyst",
    system_prompt="You are a stock analyst. Your task is to analyze companies based on recent news and reports, providing numeric data from the latest sources. You will perform market research, financial health evaluation, and risk assessment.",
    model="openai/gpt-4o",
    company_url="https://www.goldmansachs.com/",
    company_objective="To deliver superior, long-term value to clients by identifying unique investment opportunities through exhaustive fundamental research.",
)