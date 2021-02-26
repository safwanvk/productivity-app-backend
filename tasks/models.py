from django.db import models

from users.models import User

# Create your models here.
from users.models import User
from projects.models import Project


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING,
                                null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    completed = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)

    CATEGORIES = (
        (1, 'inbox'),
        (2, 'next'),
        (3, 'maybe'),
        (4, 'project')
    )
    category = models.IntegerField(choices=CATEGORIES, default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

