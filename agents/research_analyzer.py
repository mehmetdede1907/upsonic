# agents/research_analyzer_agent.py

from upsonic import Agent

research_analyst_agent = Agent(
    name="Research Analyst",
    system_prompt="You are a research analyst. You will receive a stock analysis report and your job is to synthesize this data to provide a deeper investment analysis and risk evaluation.",
    model="openai/gpt-4o",
    company_url="https://www.goldmansachs.com/",
    company_objective="To deliver superior, value to clients by identifying unique investment opportunities through exhaustive fundamental research.",
)