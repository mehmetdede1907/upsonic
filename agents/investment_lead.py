# agents/investment_lead_agent.py

from upsonic import Agent

investment_lead_agent = Agent(
    name="Investment Lead",
    system_prompt="You are an investment lead. Based on the provided investment and risk analysis, you will develop a portfolio strategy, articulate the investment rationale, and prepare a final recommendation.",
    model="openai/gpt-4o",
    company_url="https://www.goldmansachs.com/",
    company_objective="To deliver superior, value to clients by identifying unique investment opportunities through exhaustive fundamental research.",
)