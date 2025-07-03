# Stock Analyzer

A Python-based stock analysis tool that uses AI to analyze market positions, financial health, and risk assessment for companies.

## Features

- Market research analysis
- Financial health evaluation
- Risk assessment
- Web search integration for real-time data

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Run the analyzer:**
   ```bash
   python stock_anlayzer.py
   ```

## Configuration

You can modify the `company_names` list in `stock_anlayzer.py` to analyze different companies.

## Notes

- The tool includes rate limiting protection to avoid API limits
- Uses DuckDuckGo search for web data retrieval
- Requires OpenAI API key for AI analysis

## Troubleshooting

If you encounter rate limiting errors, wait a few minutes before running again.