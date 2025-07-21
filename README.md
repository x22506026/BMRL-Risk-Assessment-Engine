# BMRL Risk Assessment Engine

A simple, rule-based tool to help early-stage startup founders, incubators, and educators spot the biggest risks in a business model and get actionable recommendations.

---

## Overview

The **Business Model Risk Lens (BMRL)** evaluates a startup’s business model by asking six key questions inspired by the Business Model Canvas. Each answer carries a risk score (1 = low, 5 = high), and the tool averages them into a single rating and supplies tailored advice.

This approach gives founders a quick way to understand their structural weaknesses before investing more time or money.

---

## Business Goals

* **Rapid feedback:** Let users gauge risk in under 30 seconds.
* **Actionable guidance:** Provide clear, section-specific recommendations.
* **Ease of maintenance:** Store all scoring rules in an external CSV, so non-developers can tweak advice without touching the code.

---

## Scope

This project covers:

1. **User interface:** A single-page form where users select one option for each of six BMC-inspired questions.
2. **Risk engine:** A Flask backend that loads `rules.csv`, computes scores, maps them to labels (No/Very Low, Low, Moderate, High, Very High), and returns JSON.
3. **Recommendations:** Three top recommendations displayed based on the user’s score and selected options.

What this project does **not** include:

* User authentication or data storage beyond the session.
* Machine-learning or predictive analytics—only transparent, rule-based logic.

---

## System Architecture

Below is a view of how requests flow through BMRL:

1. **Browser** renders the form (`index.html`).  
2. User submits answers → **POST** to `/evaluate`.  
3. **Backend** (`app.py`) reads `rules.csv`, looks up weights and recommendations.  
4. Scores are averaged into a 1–5 integer, mapped to a label, and returned as JSON.  
5. **Frontend** displays the overall risk rating and the top 3 recommendations.


1. **Browser** renders the form (`index.html`).
2. User submits answers → **POST** to `/evaluate`.
3. **Backend** (`app.py`) reads `rules.csv`, looks up weights and recommendations per answer.
4. Scores are averaged into a 1–5 integer, mapped to a label, and a JSON response is returned.
5. **Frontend** displays the overall risk rating and the top 3 recommendations.

---

## Functional Requirements

| ID   | Requirement                                                | Implementation Location         |
| ---- | ---------------------------------------------------------- | ------------------------------- |
| FR‑1 | Present six dropdown questions to the user                 | `templates/index.html`          |
| FR‑2 | Send user answers as JSON to `/evaluate`                   | `static/js/app.js` or inline JS |
| FR‑3 | Load `rules.csv` at startup and map option → weight + text | `app.py: load_rules()`          |
| FR‑4 | Calculate average score (1–5), map to label, return JSON   | `app.py: evaluate()`            |

---

## Non‑Functional Requirements

* **Performance:** 95% of evaluations must complete under 200 ms.
* **Reliability:** Target uptime of 99.9%.
* **Maintainability:** All scoring rules live in `rules.csv`; no code changes needed to update advice.
* **Usability:** Simple, mobile-responsive form with live hints under each dropdown.

---

## Error Handling

* If **`rules.csv`** fails to load, the application logs an error and exits startup.
* If an incoming POST contains invalid or unexpected fields, the API returns HTTP 400 with a JSON error message:

  ```json
  { "error": "Invalid input: unknown question IDs or options." }
  ```

---

## Running the App

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the server**

   ```bash
   flask run   # or `streamlit run app.py` if using Streamlit
   ```

3. Open your browser at `http://localhost:5000` and answer the six questions.

---

## Project Structure

```
/engine/           # Scoring logic and rule definitions
/ui/               # Frontend templates and static assets
/tests/            # Automated pytest cases for /evaluate endpoint
rules.csv          # CSV of (section, option, weight, recommendation)
app.py             # Flask entry point
README.md          # This document
docs/              # Supplementary docs (architecture diagram, specs)
```

---

## Features

* Six BMC-inspired dropdown questions with live hints.
* Composite risk score (1–5) and text label.
* Top three tailored recommendations.
* Fully transparent, rule-based engine—no hidden AI.

---

## Use Cases

* **Startup founders** testing new business ideas.
* **Incubators** screening proposals quickly.
* **Educators** demonstrating business-model risk factors.

---

## License

This project is for academic and demonstration purposes only and no licneses were aquired from any main sources or third parties.
