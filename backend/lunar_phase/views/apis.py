from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import views
from rest_framework.response import Response
from ..services import Moon


class CurrentPhaseDetailAPI(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        timezone = self.request.GET.get('timezone', 'Asia/Kolkata')
        moon = Moon(tz=timezone)
        phase = moon.get_moon_phase()
        data = {"status": True, "current_phase": phase}
        return Response(data)
