import datetime
import os

def log(msg):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open("reports/log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {msg}\n")