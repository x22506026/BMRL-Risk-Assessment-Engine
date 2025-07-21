from flask import Flask, request, jsonify, render_template
import csv

app = Flask(__name__)

# Load rules from CSV at startup
RULES = []
with open('rules.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert weight to int
        row['weight'] = int(row['weight'])
        RULES.append(row)

def evaluate_section(section, input_text):
    """
    Look up the exact row in RULES matching section + option.
    Returns (weight_0_to_5, [recommendation]).
    """
    for r in RULES:
        if r['section'] == section and r['option'] == input_text:
            return min(r['weight'], 5), [r['recommendation']]
    # If no rule found, return zero risk
    return 0, []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    total_raw = 0
    section_recs = {}

    # Sum weights from CSV for each answer
    for section, answer in data.items():
        w, recs = evaluate_section(section, answer)
        total_raw += w
        section_recs[section] = recs

    # Average out of 5, rounded to whole
    avg = round(total_raw / len(data))
    avg = max(1, min(5, avg))

    # Map to label
    labels = {
        1: "No/Very Low Risk",
        2: "Low Risk",
        3: "Moderate Risk",
        4: "Risky",
        5: "High Risk"
    }

    return jsonify({
        "score": avg,
        "label": labels[avg],
        "recommendations": section_recs
    })

if __name__ == '__main__':
    app.run(debug=True)
