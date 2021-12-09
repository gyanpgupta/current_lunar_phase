from .views import CurrentLunarPhase, CurrentPhaseDetailAPI
from django.contrib.auth.decorators import login_required

from django.urls import path

urlpatterns = [
    path('', (CurrentLunarPhase.as_view()), name="current_lunar_phase"),
    path('api/current_lp', (CurrentPhaseDetailAPI.as_view()), name="current_lp_api"),
]