# AI Stock Analysis System

A three-tier AI system for stock analysis and investment recommendations using Upsonic framework.

## Quick Start

**Prerequisites:**
- Upsonic requires Python >=3.10. Here's how to check your version:
  ```bash
  python3 --version
  ```
- If you need to update Python, visit [python.org/downloads](https://python.org/downloads)

1. **Create and activate virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   pip install upsonic python-dotenv pydantic
   ```

3. **Set up Google Search MCP:**
   ```bash
   cd google-search-mcp
   npm install
   npm run build
   chmod 755 dist/index.js
   cd ..
   ```

4. **Set up Google Cloud APIs:**
   - **Enable Custom Search API:**
     - Go to [Google Cloud Console](https://console.cloud.google.com/)
     - Navigate to **APIs & Services** → **Library**
     - Search for **"Custom Search API"** and **Enable** it
   - **Create API Key:**
     - Go to **APIs & Services** → **Credentials**
     - Click **"Create Credentials"** → **"API Key"**
     - Copy the API key
   - **Create Search Engine:**
     - Go to [Programmable Search Engine](https://programmablesearchengine.google.com/)
     - Create a new search engine
     - Copy the Search Engine ID

5. **Set up environment variables in `.env`:**
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   GOOGLE_CSE_ID=your_custom_search_engine_id_here
   ```

6. **Run analysis (Run test.py):**
test.py includes each working agent without a team. To visualize, run this.
   ```bash
   python test.py  # Run with default companies (AAPL, GOOG, ORCL)
   python main.py  # Interactive mode - enter company tickers
   ```

## System Overview

**Tier 1 - Stock Analyst**: Market research, financial health, risk assessment
**Tier 2 - Research Analyst**: Investment analysis, competitive advantages, risk evaluation  
**Tier 3 - Investment Lead**: Portfolio strategy, investment rationale, final recommendations

## Output

All reports are saved in `results/` folder:
- `stock_analysis_structured_report.md` - Market and financial analysis
- `research_analysis_report.md` - Investment potential and risk evaluation
- `investment_lead_analysis_report.md` - Portfolio strategy and recommendations

## Configuration For Demo Run with Test

**Change companies**: Modify `company_names` in `agents/stock_anlayzer.py`
```python
company_names = ["AAPL", "GOOGL", "MSFT"]
```

**Custom analysis**: Adjust prompts in agent `system_prompt` parameters

## Project Structure

```
├── main.py                      # Main execution
├── test.py                      # Test all components  
├── agents/                      # AI Agent modules
│   ├── __init__.py             # Package initialization
│   ├── stock_anlayzer.py       # Tier 1: Stock analysis
│   ├── research_analyzer.py    # Tier 2: Research analysis
│   └── investment_lead.py      # Tier 3: Investment recommendations
├── helper.py                   # File utilities
├── results/                    # Generated reports
└── google-search-mcp/          # Search integration
```

## Troubleshooting
- **MCP error**: If you encounter MCP connection issues, check the `google-search-mcp/index.ts` and `google-search-mcp/dist/index.js` files. Remove the outer parentheses from the capabilities object:
  ```json
  capabilities: {
      tools: {},
  }
  ```
- **API errors**: Check `.env` file and API keys
- **Rate limits**: Wait between runs
- **Import errors**: Ensure virtual environment is activated
- **Virtual environment issues**: 
  - Make sure to activate the virtual environment before running the application
  - To deactivate: `deactivate`
  - If you get permission errors, try: `python3 -m venv venv`

---

## TODO - Current Fixed

1. **Dynamic Configuration**: The stock analysis tasks are static and don't receive company information from main.py. Implement a class hierarchy or solution to make tasks dynamic.

2. **Rate Limiting & Token Optimization**: Currently runs in test mode. Main.py needs rate limiting due to large context lengths. Make the agent structure efficient to stay under 128k tokens and avoid API limits, and run the agents in a team rather than separately in a test file. 

---

**Note**: For analysis purposes only. Not financial advice.

