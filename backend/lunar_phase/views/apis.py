from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import views
from rest_framework.response import Response
from ..services import Moon
from django.conf import settings


class CurrentPhaseDetailAPI(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        timezone = self.request.GET.get('timezone', None)
        timezone = timezone if timezone else settings.TIME_ZONE
        moon = Moon(tz=timezone)
        phase = moon.get_moon_phase()
        data = {"status": True, "current_phase": phase, "timezone": timezone}
        return Response(data)
