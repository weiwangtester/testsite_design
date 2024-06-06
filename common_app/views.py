from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProjectInfo, TestCase
from .serializers import ProjectInfoSerializer, TestCaseSerializer


# Create your views here.

class ProjectInfoViewSet(APIView):
    def get(self, request):
        queryset = ProjectInfo.objects.all()
        serializer = ProjectInfoSerializer(queryset, many=True)
        return Response(serializer.data)


class TestCaseViewSet(APIView):
    def get(self, request):
        queryset = TestCase.objects.all()
        serializer = TestCaseSerializer(queryset, many=True)
        return Response(serializer.data)
