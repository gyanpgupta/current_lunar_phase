from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CurrentLunarPhase(LoginRequiredMixin, TemplateView):
    template_name = "lunar_phase/current_lunar_phase.html"
