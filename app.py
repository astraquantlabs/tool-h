from flask import Flask, render_template, request
from scanner import scan_network
from ai import ask_ai
from security import check_password
from system_info import get_system
from report import save_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    devices = scan_network()
    system = get_system()

    ai_response = ""
    password_result = ""

    if request.method == "POST":
        query = request.form.get("query")
        password = request.form.get("password")

        if query:
            ai_response = ask_ai(query)

        if password:
            password_result = check_password(password)

    # Save report
    save_report({"devices": devices, "system": system})

    return render_template("index.html",
                           devices=devices,
                           system=system,
                           ai=ai_response,
                           password=password_result)

app.run(host="0.0.0.0", port=5000)