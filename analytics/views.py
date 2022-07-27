
from django.shortcuts import render
from django.views.generic import TemplateView


class TopTemplateView(TemplateView):
    template_name = "analytics/top.html"

