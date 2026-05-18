# BCG-GEN-AI-FORAGE-2026
AI-powered financial chatbot analyzing SEC 10-K filings — BCG GenAI Job Simulation (Forage)
# BCG GenAI Job Simulation — Forage (2026)

## Overview
Analyzing corporate financial performance from SEC 10-K filings for Microsoft, Tesla, and Apple (2023–2025) powered with chatbot.

## Steps and Progress

### Task 1 — Financial Data Analysis
- Extracted financial data from SEC EDGAR 10-K filings (reading, understanding, and filtering)
- Analyzed Total Revenue, Net Income, Total Assets,  Total Liabilities, and Cash Flow from Operations
- Calculated year-over-year growth rates and CAGR
- Visualized trends using Jupyternotebook (pandas, matplotlib)

### Task 2 — AI-Powered (Claude) Financial Chatbot
- Built a rule-based chatbot in Python
- Supports 15 predefined financial queries
- Guided session flow: select company → fiscal year → query
- Features: number input, comma-separated multi-query, 
  and 'all' command to run all queries at once

## Tools Used
- Python, pandas, matplotlib
- Claude, Perplexity
- Jupyter Notebook
- SEC EDGAR (10-K filings)

## Key Findings
- **Microsoft** — strongest performer, revenue CAGR +15.30% (2023–2025)
- **Apple** — stable growth, net income recovered to $112,010M in 2025
- **Tesla** — significant margin compression, net income CAGR -49.26%

## Files
- `financial_chatbot.py` — chatbot source code
- `GEN_AI_TASK_1_nicholas_ciputra.html` — full data analysis notebook
- `chatbot_documentation.md` — chatbot documentation

