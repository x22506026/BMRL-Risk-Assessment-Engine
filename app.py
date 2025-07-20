from flask import Flask, request, jsonify, render_template
import json

#start the flask app
app = Flask(__name__)

#load rules from JSON when the app starts
with open('rules.json', encoding='utf-8') as f:
    RULES = json.load(f)

#evaluate a single section of the BMC against all rules
def evaluate_section(input_text):
    score = 0
    recs = []
    for r in RULES:
        if eval(r['condition'], {}, {'input_text': input_text}):
            score += r['weight']
            recs.append(r['recommendation'])
    #normalize to 0–10, round to .5 steps, force minimum of 1 and max of 10
    max_score = len(RULES) * max(r['weight'] for r in RULES)
    normalized = round(((score / max_score) * 10) * 2) / 2
    normalized = max(1, min(normalized, 10))

    #assign risk category based on the score
    if normalized < 3.5:
        risk_level = "Low Risk"
    elif 3.5 <= normalized < 7:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    return normalized, risk_level, recs

#route for the homepage, shows input form
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

#route to handle evaluation requests
@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    result = {'scores': {}, 'risk_levels': {}, 'recommendations': {}, 'total_risk': 0, 'overall_level': ""}
    total = 0

    for section, text in data.items():
        sc, level, recs = evaluate_section(text)
        result['scores'][section] = sc
        result['risk_levels'][section] = level
        result['recommendations'][section] = recs
        total += sc

    avg_score = round(total / len(data), 1)
    avg_score = max(1, min(avg_score, 10))  #keep in 1–10 range

    if avg_score < 3.5:
        overall_level = "Overall: Low Risk – your business model looks healthy."
    elif 3.5 <= avg_score < 7:
        overall_level = "Overall: Medium Risk – some areas may need attention."
    else:
        overall_level = "Overall: High Risk – significant risks detected."

    result['total_risk'] = avg_score
    result['overall_level'] = overall_level

    return jsonify(result)

#start the flask development server
if __name__ == '__main__':
    app.run(debug=True)
