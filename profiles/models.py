from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.UUIDField(default=uuid.uuid4, unique=True) 
    image = models.ImageField(default='profiles/download.jpg', upload_to='profiles/', null=True)
    group_name = models.CharField(max_length=100, null=True, blank=True)
    project_id = models.UUIDField(default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        if self.user is not None:
            return self.user.username
        return ""