from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectCreateSerializer, ProjectDetailSerializer


@api_view(['POST'])
def create_project(request):
    serializer = ProjectCreateSerializer(data=request.data)
    if serializer.is_valid():
        project = serializer.save()
        response_serializer = ProjectDetailSerializer(project)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
