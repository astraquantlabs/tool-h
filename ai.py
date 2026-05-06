def ask_ai(query):
    query = query.lower()

    if "port" in query:
        return "Ports are communication endpoints. Open ports may expose services."

    elif "secure" in query:
        return "Use strong passwords, firewall, and avoid public WiFi."

    elif "scan" in query:
        return "Scanning helps detect devices in your network."

    return "Tool-H AI: Ask about networks or security."