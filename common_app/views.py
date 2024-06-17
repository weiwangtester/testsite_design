from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProjectInfo, TestCase
from .serializers import ProjectInfoSerializer, TestCaseSerializer
from celery import shared_task
from . import tasks


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


def celery_demo(request):
    if request.method == "GET":
        x = request.GET.get("x", 0) or 0
        y = request.GET.get("y", 0) or 0
    elif request.method == "POST":
        x = request.POST.get("x", 0) or 0
        y = request.POST.get("y", 0) or 0
    else:
        return Response("params error")
    try:
        tasks.demo_add.delay(int(x), int(y))
    except ValueError as e:
        print(e)
        return Response("params error")
    return Response("celery demo test")
