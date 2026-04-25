# Personal Finance Tracker

A terminal-based personal finance management tool built with Python. Track income, expenses, savings goals, and generate visual reports, all from the command line.

---

## Features

- **Transaction Management** — Log income and expenses by category with optional descriptions
- **Recurring Expenses** — Mark bills as recurring and apply them automatically each month
- **Savings Goals** — Set financial targets and track progress over time
- **Visual Charts** — Generate spending breakdowns, income vs expense comparisons, and savings progress charts using Matplotlib
- **PDF Reports** — Export a full financial summary as a dated PDF report using ReportLab
- **SQLite Storage** — All data is stored locally in a lightweight SQLite database, no internet required

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Database | SQLite3 (built-in) |
| Charts | Matplotlib |
| PDF Export | ReportLab |

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/Kxrma35/finance-tracker.git
cd finance-tracker
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv
```
On Windows:
```bash
.venv\Scripts\activate
```
On macOS/Linux:
```bash
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install matplotlib reportlab
```

---

## Usage

Run the app with:
```bash
python main.py
```

On first run the database is automatically created. You will be presented with a menu to add transactions, manage savings goals, view charts, and export reports.

---

## Project Structure

```
finance-tracker/
├── main.py          # Entry point and menu
├── database.py      # Database setup and connection
├── models.py        # Transaction and SavingsGoal classes
├── tracker.py       # Core business logic
├── charts.py        # Matplotlib visualizations
├── reports.py       # PDF report generation
└── finance.db       # Auto-generated SQLite database
```

---

## Charts Available

- Spending by Category — Pie chart breaking down where your money goes
- Income vs Expenses — Bar chart comparing totals at a glance
- Savings Goals Progress — Grouped bar chart showing saved vs target per goal

---

## PDF Reports

Exported reports include a financial summary, full transaction history, and savings goals progress. Reports are saved as `finance_report_YYYY-MM-DD.pdf` in the project folder.

---

## Author

Karma Kioko
- Email: karmanjeruh5@gmail.com
- Phone: 0793960550
- GitHub: https://github.com/Kxrma35

---

## License

This project is open source and available under the MIT License.
