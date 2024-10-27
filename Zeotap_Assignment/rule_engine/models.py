# models.py

from django.db import models  # type: ignore

class Rule(models.Model):
    name = models.CharField(max_length=255)
    rule_string = models.TextField()  # Stores the rule in string format
    created_at = models.DateTimeField(auto_now_add=True)

class ASTNode(models.Model):
    type = models.CharField(max_length=50)  # 'operator' or 'operand'
    left = models.ForeignKey('self', null=True, blank=True, related_name='left_node', on_delete=models.CASCADE)
    right = models.ForeignKey('self', null=True, blank=True, related_name='right_node', on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True, blank=True)  # Operand values if applicable
