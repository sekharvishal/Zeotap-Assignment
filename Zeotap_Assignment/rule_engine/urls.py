# urls.py

from django.urls import path  # type: ignore
from .views import create_rule, combine_rules, evaluate_rule

urlpatterns = [
    path('create_rule/', create_rule, name='create_rule'),
    path('combine_rules/', combine_rules, name='combine_rules'),
    path('evaluate_rule/', evaluate_rule, name='evaluate_rule'),
]
