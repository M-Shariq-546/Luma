from django.conf import settings
from django.db import models
from profiles.models import Profile
from datetime import timezone
import uuid

class Conversation(models.Model):
    chatroom_name = models.CharField(max_length=200, null=True , blank=True)
    sender = models.ForeignKey(Profile, related_name='sender', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    chatroom = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    receiver = models.ForeignKey(Profile, related_name='receiver', on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.chatroom_name)
    
        
    
class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='message_sender', on_delete=models.CASCADE, null=True, blank=True)
    message_body = models.CharField(max_length=500, null=True ,blank=True)
    attachments = models.FileField(blank=True , upload_to="attachments/")
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True , blank=True)
    profile_image = models.ImageField(default='profiles/default.jpg' , upload_to="profile_images/")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.conversation.chatroom_name #"sender ===> "+str(self.sender)+"| sends ===> "+str(self.message_body)
    
    class Meta:
        ordering = ["-timestamp"]
