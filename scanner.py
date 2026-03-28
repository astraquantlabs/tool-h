import os
import datetime

def scan(target):
    result = os.popen(f"nmap -sV {target}").read()

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/{target}.txt"

    with open(filename, "w") as f:
        f.write(f"Scan Report for {target}\n")
        f.write(result)

    return result