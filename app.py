from flask import Flask, render_template, request, jsonify
from scanner import scan
from ai import ai_reply
from visualizer import draw_network
from logger import log

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def do_scan():
    target = request.json["target"]
    log(f"Scan started on {target}")
    result = scan(target)
    return jsonify({"result": result})

@app.route("/ai", methods=["POST"])
def ai():
    msg = request.json["msg"]
    reply = ai_reply(msg)
    return jsonify({"reply": reply})

@app.route("/visualize")
def visualize():
    draw_network()
    return {"status": "Network map generated"}

if __name__ == "__main__":
    app.run(debug=True)