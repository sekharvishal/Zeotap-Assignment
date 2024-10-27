# __init__.py

# Importing models
from .models import Rule, ASTNode

# Importing views (or functions)
from .views import create_rule, combine_rules, evaluate_rule

# Expose public API
__all__ = [
    'Rule',
    'ASTNode',
    'create_rule',
    'combine_rules',
    'evaluate_rule',
]

# Optional: Initialize any necessary settings or configurations here
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Rule Engine package initialized.")
