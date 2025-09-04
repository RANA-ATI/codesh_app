from django.db import models
from django.core.validators import EmailValidator


class Project(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'
        ordering = ['-created_at']
