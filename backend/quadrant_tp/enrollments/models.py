from django.db import models
from django.core.validators import EmailValidator
from projects.models import Project


class Enrollment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()])
    start_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='enrollments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.project.name}"

    class Meta:
        db_table = 'enrollments'
        ordering = ['-created_at']
        unique_together = ['email', 'project']
