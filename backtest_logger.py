import csv
from datetime import datetime

FILE = "backtest_log.csv"

def log_bet(game, market, pick, line, projection):
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            game,
            market,
            pick,
            line,
            projection
        ])
