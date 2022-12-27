"""
Views from app music
"""
from django.views.generic import TemplateView


class Homepage(TemplateView):
    """return basic html template homepage"""
    template_name = "homepage.html"
