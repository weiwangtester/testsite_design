from rest_framework import serializers
from .models import ProjectInfo, TestCase


class ProjectInfoSerializer(serializers.ModelSerializer):
    """自定义 Project 对象如何序列化"""

    class Meta:
        model = ProjectInfo
        fields = '__all__'  # 或指定需要序列化的字段


class TestCaseSerializer(serializers.ModelSerializer):
    """自定义 ProjectATestCase 对象如何序列化"""

    class Meta:
        model = TestCase
        fields = '__all__'  # 或指定需要序列化的字段
