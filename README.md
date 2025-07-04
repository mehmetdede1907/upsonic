# AI Stock Analysis System

A three-tier AI system for stock analysis and investment recommendations using Upsonic framework.

## Quick Start

1. **Install Python dependencies:**
   ```bash
   pip install upsonic python-dotenv pydantic
   ```

2. **Set up Google Search MCP:**
   ```bash
   cd google-search-mcp
   npm install
   npm run build
   chmod 755 dist/index.js
   cd ..
   ```

3. **Set up Google Cloud APIs:**
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

4. **Set up environment variables in `.env`:**
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   GOOGLE_CSE_ID=your_custom_search_engine_id_here
   ```

5. **Run analysis:**
for now run the test code to not exeed 4o token rate limit
   ```bash
   python main.py  # Interactive mode - enter company tickers
   python test.py  # Run with default companies (AAPL, GOOG, ORCL)
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

## Configuration For Demo Run with Tes

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

- **API errors**: Check `.env` file and API keys
- **Rate limits**: Wait between runs
- **Import errors**: Ensure virtual environment is activated

---

## TODO - Current Bugs Need To Be Fixed

1. **Dynamic Company Configuration**: The stock analysis tasks are static and don't receive company information from main.py. Implement a class hierarchy or solution to make tasks dynamic.

2. **Rate Limiting & Token Optimization**: Currently runs in test mode. Main.py needs rate limiting due to large context lengths. Make it efficient to stay under 128k tokens and avoid API limits.

---

**Note**: For analysis purposes only. Not financial advice.

