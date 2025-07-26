import csv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# loading csv of rules into memory at startup
def load_rules(path="rules.csv"):
    rules = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            section = row["section"]
            option = row["option"]
            weight = int(row["weight"])
            rec = row["recommendation"]
            rules[(section, option)] = (weight, rec)
    return rules

# in-memory store of all (section, option) → (weight, recommendation)
RULES = load_rules()

# route to serve the main risk‑assessment form
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# route to process JSON payload and return risk score + recommendations
@app.route("/evaluate", methods=["POST"])
def evaluate():
    # parsing incoming JSON payload
    data = request.get_json() or {}
    # validation: must have exactly six answers
    if not isinstance(data, dict) or len(data) != 6:
        return jsonify(error="Invalid input: exactly 6 answers required."), 400

    total_weight = 0
    recs = []
    # computing total weight and collecting recommendations
    for section, answer in data.items():
        key = (section, answer)
        if key not in RULES:
            return jsonify(error=f"Invalid answer for section '{section}'."), 400
        weight, recommendation = RULES[key]
        total_weight += weight
        recs.append(recommendation)

    # computing average score (1–5) and mapping to label
    avg = round(total_weight / len(data))
    labels = {
        1: "No/Very Low Risk",
        2: "Low Risk",
        3: "Moderate Risk",
        4: "High Risk",
        5: "Very High Risk"
    }
    label = labels.get(avg, "Unknown")

    # returning JSON response with score, label, and six recommendations
    return jsonify(score=avg, label=label, recommendations=recs), 200

if __name__ == "__main__":
    # start Flask app on all interfaces, debug mode for development
    app.run(host="0.0.0.0", port=5000, debug=True)
