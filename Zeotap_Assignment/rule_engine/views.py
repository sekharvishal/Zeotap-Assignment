# views.py

import json
import re
from django.http import JsonResponse  # type: ignore
from .models import Rule, ASTNode

def create_rule(rule_string):
    tokens = re.findall(r'(\w+|\S)', rule_string)  # Simple tokenization
    root = parse_tokens(tokens)
    return root

def parse_tokens(tokens):
    # Implement a more sophisticated parser that handles operators and nested expressions
    stack = []
    for token in tokens:
        if token in ('AND', 'OR'):
            right = stack.pop()
            left = stack.pop()
            node = ASTNode.objects.create(type="operator", value=token)
            node.left = left
            node.right = right
            node.save()
            stack.append(node)
        else:
            node = ASTNode.objects.create(type="operand", value=token)
            stack.append(node)
    return stack.pop() if stack else None

def combine_rules(rules):
    # Combine rules into a single AST
    combined = ASTNode.objects.create(type="operator")  # Root node for combined rules
    for rule in rules:
        ast = create_rule(rule)
        # Logic to combine ASTs; for now, we simply connect the roots
        combined.left = ast  # Example logic; modify as needed
    combined.save()
    return combined

def evaluate_rule(ast, data):
    # Evaluate the AST against provided user data
    if ast.type == "operand":
        # Simplified evaluation
        return data.get(ast.value)  # Implement proper logic

    if ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        # Combine results based on operator type (AND/OR)
        if ast.value == 'AND':
            return left_result and right_result
        elif ast.value == 'OR':
            return left_result or right_result

    return False  # Default case
