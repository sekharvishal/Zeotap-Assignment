# tests.py

from django.test import TestCase  # type: ignore
from .models import Rule, ASTNode
from .views import create_rule, combine_rules, evaluate_rule

class RuleEngineTests(TestCase):
    
    def setUp(self):
        # Set up initial test data
        self.rule1_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        self.rule2_string = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
        
        # Create rules in the database
        self.rule1 = Rule.objects.create(name="Rule 1", rule_string=self.rule1_string)
        self.rule2 = Rule.objects.create(name="Rule 2", rule_string=self.rule2_string)

    def test_create_rule(self):
        ast = create_rule(self.rule1.rule_string)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.type, "operator")  # Adjust based on expected AST structure

    def test_combine_rules(self):
        combined_ast = combine_rules([self.rule1.rule_string, self.rule2.rule_string])
        self.assertIsNotNone(combined_ast)
        self.assertEqual(combined_ast.type, "operator")  # Check the combined AST type

    def test_evaluate_rule(self):
        ast = create_rule(self.rule1.rule_string)
        user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        result = evaluate_rule(ast, user_data)
        self.assertTrue(result)

    def test_invalid_rule(self):
        with self.assertRaises(ValueError):
            create_rule("INVALID RULE STRING")
