from rest_framework import serializers
from .models import Project


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'start_date']
        read_only_fields = ['id']


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'start_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']