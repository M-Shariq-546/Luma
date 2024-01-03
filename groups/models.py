#from .models import Group
from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User
from django.conf import settings
import uuid

class Group(models.Model):
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    group_name = models.CharField(max_length=200 , null=True, blank=True)
    group_id = models.UUIDField(default=uuid.uuid4 , unique=True)
    is_active = models.BooleanField(default=True)
    users = models.ManyToManyField("Members",blank=True)
    def __str__(self):
        return str(self.group_name) 

class Members(models.Model):
    group_name = models.ForeignKey(Group,related_name='group', on_delete=models.CASCADE, null=True, blank=True)
    member = models.OneToOneField(Profile, related_name='members', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    member_key = models.UUIDField(default=uuid.uuid4)
    email = models.EmailField(null=True , blank=True)
    is_invited = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)

    def __str__(self):
        return str(self.member)