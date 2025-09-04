from rest_framework import serializers
from .models import Enrollment
from projects.serializers import ProjectDetailSerializer


class EnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['name', 'email', 'start_date', 'project']

    def validate(self, data):
        if Enrollment.objects.filter(email=data['email'], project=data['project']).exists():
            raise serializers.ValidationError("User is already enrolled in this project.")
        return data


class EnrollmentDetailSerializer(serializers.ModelSerializer):
    project = ProjectDetailSerializer(read_only=True)
    
    class Meta:
        model = Enrollment
        fields = ['id', 'name', 'email', 'start_date', 'project', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class EnrollmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'name', 'email', 'start_date', 'created_at']
        read_only_fields = ['id', 'created_at']