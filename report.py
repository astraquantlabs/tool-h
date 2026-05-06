import json
import os

def save_report(data):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open("reports/report.json", "w") as f:
        json.dump(data, f, indent=4)