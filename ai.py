import os
import datetime

def ai_reply(msg):
    msg = msg.lower()

    if "time" in msg:
        return str(datetime.datetime.now())

    if "scan" in msg:
        return "Use the scan section to analyze a target IP."

    if "network" in msg:
        return "You can generate a network visualization."

    if os.getenv("API_KEY"):
        return "Real AI will be connected here later."

    return "AstraQuant AI: I am running in local mode."