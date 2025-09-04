from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Enrollment
from projects.models import Project
from .serializers import EnrollmentCreateSerializer, EnrollmentDetailSerializer, EnrollmentListSerializer


@api_view(['POST'])
def enroll_user(request):
    serializer = EnrollmentCreateSerializer(data=request.data)
    if serializer.is_valid():
        enrollment = serializer.save()
        response_serializer = EnrollmentDetailSerializer(enrollment)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_enrollments_by_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    enrollments = Enrollment.objects.filter(project=project)
    serializer = EnrollmentListSerializer(enrollments, many=True)
    return Response({
        'project': {
            'id': project.id,
            'name': project.name,
            'start_date': project.start_date
        },
        'enrollments': serializer.data
    }, status=status.HTTP_200_OK)
