from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('enroll/', views.enroll_user, name='enroll_user'),
    path('project/<int:project_id>/', views.get_enrollments_by_project, name='get_enrollments_by_project'),
]