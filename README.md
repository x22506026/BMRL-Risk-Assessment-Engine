# Business Model Risk Lens (BMRL) Assessment Engine

A rule based tool to help early stage startup founders, incubators, and stakeholders spot the biggest risks in a business model and get actionable recommendations.

---

## Overview

The **Business Model Risk Lens (BMRL)** evaluates a startup’s business model by asking six key questions inspired by the Business Model Canvas. Each answer carries a risk score (1 = low, 5 = high), and the tool averages them into a single rating and supplies tailored advice. This approach gives founders a quick way to understand their structural weaknesses before investing more time or money.

---

## Business Goals

* **Rapid feedback:** Let business officials to see results instantly.
* **Actionable guidance:** Provide clear, specific recommendations based on actual input by stakeholders.
* **Ease of development:** In future tense, after introducing new definitions, rules and inputs, this idea can help governments or investment firms as a national service or building a strong clientele.

---

## Scope

This project covers:

1. **User interface:** A single page form where users select one option for each of six BMC inspired questions.
2. **Risk engine:** A Flask backend that loads `rules.csv`, computes scores, maps them to labels (No/Very Low, Low, Moderate, High, Very High), and returns JSON.
3. **Recommendations:** Six recommendations displayed based on the user’s score and selected options.

What this project does **not** include:

* User authentication or data storage beyond the session.
* Machine learning or predictive analytics as it is only a transparent, rule based logic.

---

## Running the App

1. Open a terminal and cd into the folder containing the downloaded files.
2. (Optional) Create a virtual environment to isolate dependencies:
   python3 -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
3. Install the required Python packages:
   pip install -r requirements.txt
4. python app.py
5. http://localhost:5000



---

## Project Structure

```
/engine/           # Scoring logic and rule definitions
/ui/               # Frontend templates and static assets
/tests/            # Automated pytest cases for /evaluate endpoint
rules.csv          # CSV of (section, option, weight, recommendation)
app.py             # Flask entry point
README.md          # This document describing project and how to run
```

---

## License

This project is for academic and demonstration purposes only and no licneses were aquired from any main sources or third parties.
