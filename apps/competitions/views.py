from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .services import get_world_cup
from .serializers import CompetitionSerializer


class WorldCupView(APIView):

    @extend_schema(responses=CompetitionSerializer)
    def get(self, request):
        data = get_world_cup()
        serializer = CompetitionSerializer(data)
        return Response(serializer.data)
