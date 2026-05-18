# =============================================================================
# GFC AI-Powered Financial Chatbot Prototype
# BCG GenAI Job Simulation - Task 2
# Author: Nicholas Ciputra
# Data Source: SEC EDGAR 10-K Filings (Microsoft, Tesla, Apple) 2023-2025
# =============================================================================
 
FINANCIAL_DATA = {
    "Microsoft": {
        2023: {"Total Revenue": 211915, "Net Income": 72361, "Total Assets": 411976, "Total Liabilities": 205753, "Cash Flow from Operating Activities": 87582},
        2024: {"Total Revenue": 245122, "Net Income": 88136, "Total Assets": 512163, "Total Liabilities": 243686, "Cash Flow from Operating Activities": 118548},
        2025: {"Total Revenue": 281724, "Net Income": 101800, "Total Assets": 619000, "Total Liabilities": 275520, "Cash Flow from Operating Activities": 136200},
    },
    "Tesla": {
        2023: {"Total Revenue": 96773,  "Net Income": 14974, "Total Assets": 106618, "Total Liabilities": 43009, "Cash Flow from Operating Activities": 13256},
        2024: {"Total Revenue": 97690,  "Net Income": 7153,  "Total Assets": 122070, "Total Liabilities": 48390, "Cash Flow from Operating Activities": 14724},
        2025: {"Total Revenue": 94827,  "Net Income": 3855,  "Total Assets": 137806, "Total Liabilities": 54951, "Cash Flow from Operating Activities": 11497},
    },
    "Apple": {
        2023: {"Total Revenue": 383285, "Net Income": 96995, "Total Assets": 352583, "Total Liabilities": 290437, "Cash Flow from Operating Activities": 110543},
        2024: {"Total Revenue": 391035, "Net Income": 93736, "Total Assets": 364980, "Total Liabilities": 308030, "Cash Flow from Operating Activities": 118254},
        2025: {"Total Revenue": 416161, "Net Income": 112010, "Total Assets": 359240, "Total Liabilities": 285510, "Cash Flow from Operating Activities": 111482},
    }
}
 
YEARS = [2023, 2024, 2025]
COMPANIES = ["Microsoft", "Tesla", "Apple"]
 
QUERIES = [
    "What is the total revenue?",
    "What is the Net Income?",
    "What is the sum of total assets?",
    "What is the sum of total liabilities?",
    "What is cash flow from operating activities?",
    "What is the revenue growth(%)?",
    "What is the net income growth(%)?",
    "What is the assets growth(%)?",
    "What is the liabilities growth(%)?",
    "What is the cash flow from operations growth(%)?",
    "What is the year by year average revenue growth rate(%)?",
    "What is the year by year average net income growth rate(%)?",
    "What is the year by year average assets growth rate(%)?",
    "What is the year by year average liabilities growth rate(%)?",
    "What is the year by year average cash flow from operations growth rate(%)?",
]
 
 
def pct_change(old, new):
    if old == 0:
        return None
    return round(((new - old) / old) * 100, 2)
 
 
def avg_growth(values):
    changes = []
    for i in range(1, len(values)):
        c = pct_change(values[i-1], values[i])
        if c is not None:
            changes.append(c)
    if not changes:
        return None
    return round(sum(changes) / len(changes), 2)

def handle_query(query, company, year):
    # Allow number selection
    query = query.strip()
    if query.isdigit():
        num = int(query)
        if 1 <= num <= len(QUERIES):
            query = QUERIES[num - 1]
        else:
            return "Please enter a number between 1 and 15."

    data = FINANCIAL_DATA[company]
    years = sorted(data.keys())
    q = query.strip().lower()

    if "total revenue" in q and "growth" not in q and "average" not in q:
        val = data[year]["Total Revenue"]
        return f"The Total Revenue for {company} for fiscal year {year} is ${val:,}M"

    elif "net income" in q and "growth" not in q and "average" not in q:
        val = data[year]["Net Income"]
        return f"The Net Income for {company} for fiscal year {year} is ${val:,}M"

    elif "total assets" in q and "growth" not in q and "average" not in q:
        val = data[year]["Total Assets"]
        return f"The sum of Total Assets for {company} for fiscal year {year} is ${val:,}M"

    elif "total liabilities" in q and "growth" not in q and "average" not in q:
        val = data[year]["Total Liabilities"]
        return f"The sum of Total Liabilities for {company} for fiscal year {year} is ${val:,}M"

    elif "cash flow from operating" in q and "growth" not in q and "average" not in q:
        val = data[year]["Cash Flow from Operating Activities"]
        return f"The Cash Flow from Operating Activities for {company} for fiscal year {year} is ${val:,}M"

    elif "revenue growth" in q and "average" not in q:
        idx = years.index(year)
        if idx == 0:
            return f"No prior year available to calculate Revenue Growth for {company} in {year}."
        growth = pct_change(data[years[idx-1]]["Total Revenue"], data[year]["Total Revenue"])
        return f"The Revenue Growth (%) for {company} from {years[idx-1]} to {year} is {growth}%"

    elif "net income growth" in q and "average" not in q:
        idx = years.index(year)
        if idx == 0:
            return f"No prior year available to calculate Net Income Growth for {company} in {year}."
        growth = pct_change(data[years[idx-1]]["Net Income"], data[year]["Net Income"])
        return f"The Net Income Growth (%) for {company} from {years[idx-1]} to {year} is {growth}%"

    elif "assets growth" in q and "average" not in q:
        idx = years.index(year)
        if idx == 0:
            return f"No prior year available to calculate Assets Growth for {company} in {year}."
        growth = pct_change(data[years[idx-1]]["Total Assets"], data[year]["Total Assets"])
        return f"The Assets Growth (%) for {company} from {years[idx-1]} to {year} is {growth}%"

    elif "liabilities growth" in q and "average" not in q:
        idx = years.index(year)
        if idx == 0:
            return f"No prior year available to calculate Liabilities Growth for {company} in {year}."
        growth = pct_change(data[years[idx-1]]["Total Liabilities"], data[year]["Total Liabilities"])
        return f"The Liabilities Growth (%) for {company} from {years[idx-1]} to {year} is {growth}%"

    elif "cash flow from operations growth" in q and "average" not in q:
        idx = years.index(year)
        if idx == 0:
            return f"No prior year available to calculate CFO Growth for {company} in {year}."
        growth = pct_change(data[years[idx-1]]["Cash Flow from Operating Activities"], data[year]["Cash Flow from Operating Activities"])
        return f"The Cash Flow from Operations Growth (%) for {company} from {years[idx-1]} to {year} is {growth}%"

    elif "average revenue growth" in q:
        values = [data[y]["Total Revenue"] for y in years]
        avg = avg_growth(values)
        return f"The year by year average Revenue Growth Rate for {company} (2023-2025) is {avg}%"

    elif "average net income growth" in q:
        values = [data[y]["Net Income"] for y in years]
        avg = avg_growth(values)
        return f"The year by year average Net Income Growth Rate for {company} (2023-2025) is {avg}%"

    elif "average assets growth" in q:
        values = [data[y]["Total Assets"] for y in years]
        avg = avg_growth(values)
        return f"The year by year average Assets Growth Rate for {company} (2023-2025) is {avg}%"

    elif "average liabilities growth" in q:
        values = [data[y]["Total Liabilities"] for y in years]
        avg = avg_growth(values)
        return f"The year by year average Liabilities Growth Rate for {company} (2023-2025) is {avg}%"

    elif "average cash flow from operations growth" in q:
        values = [data[y]["Cash Flow from Operating Activities"] for y in years]
        avg = avg_growth(values)
        return f"The year by year average Cash Flow from Operations Growth Rate for {company} (2023-2025) is {avg}%"

    else:
        return "Sorry, I can only provide information on predefined queries."

 
 
def select_company():
    print("\nPlease select the company name from below:")
    for i, c in enumerate(COMPANIES, 1):
        print(f"  {i}. {c}")
    while True:
        entry = input("Enter company name: ").strip()
        if entry in COMPANIES:
            return entry
        if entry in ["1", "2", "3"]:
            return COMPANIES[int(entry) - 1]
        print("Invalid input. Please enter Microsoft, Tesla, or Apple.")
 
 
def select_year(company):
    available = sorted(FINANCIAL_DATA[company].keys())
    print(f"\nThe data for fiscal years {', '.join(str(y) for y in available)} is currently available.")
    while True:
        entry = input(f"Enter fiscal year ({available[0]}-{available[-1]}): ").strip()
        try:
            year = int(entry)
            if year in available:
                return year
        except ValueError:
            pass
        print(f"Invalid year. Please enter one of: {available}")
 
 
def show_queries():
    print("\nAvailable queries:")
    for i, q in enumerate(QUERIES, 1):
        print(f"  {i:>2}. {q}")
 
 
def run_session():
    print("\nHWelcome to AI Driven Financial Chatbot!!!")
    print("What can i help you with your financial queries?")
 
    company = select_company()
    year = select_year(company)
    print(f"\nThe fiscal year for the selected company: {year}")
 
    show_queries()
 
    while True:
        query = input("\nPlease enter your query (or 'reset' to restart, 'exit' to quit):\n> ").strip()
        if query.lower() == "exit":
            return False
        elif query.lower() == "reset":
            return True
        elif query == "":
            continue
        elif query.lower() == "all":
            print("\n--- Running all queries ---")
            for i, q in enumerate(QUERIES, 1):
                response = handle_query(q, company, year)
                print(f"\n{i}. {q}")
                print(f"   {response}")
        elif "," in query:
            parts = [p.strip() for p in query.split(",")]
            print("\n--- Running selected queries ---")
            for part in parts:
                response = handle_query(part, company, year)
                if part.isdigit():
                    num = int(part)
                    if 1 <= num <= len(QUERIES):
                        print(f"\n{num}. {QUERIES[num-1]}")
                else:
                    print(f"\n{part}")
                print(f"   {response}")
        else:
            response = handle_query(query, company, year)
            print(f"\n{response}")
 
if __name__ == "__main__":
    print("=" * 60)
    print("  GFC Financial Chatbot — BCG GenAI Simulation Task 2")
    print("  Data: Microsoft, Tesla, Apple | 10-K Filings 2023-2025")
    print("=" * 60)
 
    while True:
        entry = input("\nEnter 'Hi' to start the chatbot session (or 'exit' to quit): ").strip().lower()
        if entry == "exit":
            print("Chatbot: Goodbye!")
            break
        elif entry == "hi":
            continue_session = run_session()
            if not continue_session:
                print("Chatbot: Goodbye!")
                break
        else:
            print("Please type 'Hi' to begin or 'exit' to quit.")