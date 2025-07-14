from flask import Flask, request, jsonify, render_template
import json

#proposing the Flask application
app = Flask(__name__)

#load risk rules into memory at startup
with open('rules.json') as f:
    RULES = json.load(f)

#evaluate a single BMC section's text against all rules
#returns a normalized score (0–10) and a list of recommendation strings
#loop through each rule, check the condition, add its penalty to the score,
#collect its recommendation if triggered, then scale the total to 0–10.
def evaluate_section(input_text):
    score, recs = 0, []
    for r in RULES:
        #check each rule condition against the input text
        if eval(r['condition'], {}, {'input_text': input_text}):
            score += r['weight']
            recs.append(r['recommendation'])
    #determine max possible score for normalization
    max_score = len(RULES) * max(r['weight'] for r in RULES)
    normalized = round((score / max_score) * 10, 2)
    return normalized, recs

#serving the HTML form for BMC input
@app.route('/', methods=['GET'])
def home():
    #render index.html from the templates folder
    return render_template('index.html')

#process JSON payload with BMC data and returning the risk analysis
@app.route('/evaluate', methods=['POST'])
def evaluate():
    #parsing the incoming JSON payload of nine BMC fields
    data = request.get_json()
    result = {'scores': {}, 'recommendations': {}, 'total_risk': 0}
    total = 0

    #to evaluate each section and accumulate results
    for section, text in data.items():
        sc, recs = evaluate_section(text)
        result['scores'][section] = sc
        result['recommendations'][section] = recs
        total += sc

    #compute the overall risk score
    result['total_risk'] = round(total / len(data), 2)
    return jsonify(result)

#running the development server in debug mode
if __name__ == '__main__':
    app.run(debug=True)
