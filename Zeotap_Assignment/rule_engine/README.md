Rule Engine Project Overview

The Rule Engine project is a 3-tier application designed to evaluate user eligibility based on attributes such as age, department, income, and experience using an Abstract Syntax Tree (AST) representation of rules. It features functionalities for dynamic rule creation, combination, and evaluation, with rules defined in string format.

Key Features:

Dynamic creation of rules in string format, converted into an AST.
Combination of multiple rules into a single AST.
Evaluation of user data against the defined rules to determine eligibility.
Robust error handling for invalid rules and inputs.
Data Structure:

The AST is represented using nodes that can be "operator" (AND/OR) or "operand" (conditions).
type: Indicates the node type ("operator" or "operand").
left: Reference to the left child node.
right: Reference to the right child node.
value: Optional value for operand nodes (e.g., comparison values).
Installation Steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/rule-engine.git
cd rule-engine
Set up a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
API Endpoints:

Create a Rule: POST /create_rule/ with body { "rule_string": "YOUR_RULE_STRING" }.
Combine Rules: POST /combine_rules/ with body { "rules": ["RULE_STRING_1", "RULE_STRING_2"] }.
Evaluate Rule: POST /evaluate_rule/ with body { "ast": "AST_NODE", "data": { "age": 35, "department": "Sales", "salary": 60000, "experience": 3 } }.
Testing: Run tests using:

bash
Copy code
python manage.py test