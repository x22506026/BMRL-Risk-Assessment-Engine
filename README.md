# BMRL-Risk-Assessment-Engine
Rule-based engine to assess startup business model risks.

# Business Model Risk Lens (BMRL)

## Overview
The Business Model Risk Lens (BMRL) is a rule-based logic engine designed to evaluate early-stage startup business models. By accepting structured input aligned with the Business Model Canvas framework, the tool calculates a composite risk score and offers targeted recommendations for improvement.

BMRL aims to support startup founders, incubators, and educators in identifying structural weaknesses before scaling or investment.

## Technologies Used
- Python
- Streamlit
- GitHub (version control)
- Trello (task management)

## How to Run
1. Install requirements:
   ```bash
   pip install streamlit
   ```

2. Run the application:
   ```bash
   streamlit run app.py
   ```

## Project Structure
```
/engine/           # Contains rule logic for scoring and analysis
/ui/               # Contains Streamlit frontend components
/test_profiles/    # Sample structured inputs for testing
utils.py           # Helper functions for risk processing
app.py             # Main Streamlit application
README.md          # Project description and usage guide
```

## Features
- Accepts user input across all 9 BMC sections
- Scores individual components and generates a total risk rating
- Provides section-specific recommendations for improvement
- Transparent rule-based design (no black-box ML)

## Use Case
- Early-stage startups evaluating their models
- Incubators screening proposals
- Entrepreneurship educators teaching business structure

## License
This project is for academic purposes only.
