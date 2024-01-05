from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from profiles.models import Profile
import uuid
from django.conf import settings

class Task(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    project_id = models.ForeignKey('Project', null=True,on_delete=models.CASCADE)
    director = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name    


class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    director = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    project_id = models.UUIDField(default=uuid.uuid4, editable=False)
    tasks = models.ManyToManyField(Task)
    is_active = models.BooleanField(default=True)
    project_name = models.CharField(max_length=200, null=True, blank=True)
    assigned_to = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='assigned', on_delete=models.CASCADE, blank=True)
    due_date = models.DateTimeField(auto_now_add=True)
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]

    color = ColorField(samples=COLOR_PALETTE)
    color = ColorField(choices=COLOR_PALETTE)
    
    def __str__(self):
        return self.project_name