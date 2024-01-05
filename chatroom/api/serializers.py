from profiles.api.serializers import ProfileSerializer
from rest_framework import serializers
from rest_framework.serializers import FileField
from chatroom.models import Conversation, Message

class ConverstaionSerializers(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields =[
            'chatroom_name',
            'chatroom',
            'created_date',
        ]
        
    def get_sender(self , obj):
        return obj.sender.username

    def get_receiver(self , obj):
        return obj.receiver.username
    
    def get_created_date(self , obj):
        return obj.created_date.strftime('%d-%m-%Y %I:%M %p')
    
    
class CreateConverstaionSerializers(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields =[
            'chatroom_name',
            'sender',
            'receiver',
            'created_date'
        ]
    
    def get_sender(self , obj):
        if obj.sender is not None:
            return obj.sender.username
        else:
            return ''

    def get_created_date(self , obj):
        return obj.created_date.strftime('%d-%m-%Y %I:%M %p') 

    def get_receiver(self , obj):
        if obj.receiver is not None:
            return obj.receiver.username
        else:
            return ''
    
    def get_sender_profile_image(self , obj):
        if obj.sender is not None:
            return obj.sender.url
        else:
            return ''
    
    def get_receiver_profile_image(self , obj):
        if obj.receiver is not None:
            return obj.receiver.url
        else:
            return ''
                    
class MessageSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()
    sender = ProfileSerializer()
    class Meta:
        model = Message
        fields = [
            'sender',
            'message_body',
            'attachments',
            'timestamp',
        ]
        
        read_only_field = ['message_body']
    
    def get_queryset(self, obj):
        conversation = obj.chatroom
        print(conversation)
        messages = Message.objects.filter(conversation__chatroom=conversation)
        return messages
    
    
    def get_attachments(self , obj):
        if obj is not None:
            return obj.attachments
        return ""
    
    def get_timestamp(self , obj):
        return obj.timestamp.strftime('%d-%m-%Y %I:%M %p')
        
class MessageInboxSerializer(serializers.ModelSerializer):
    attachments = FileField()
    class Meta:
        model = Message
        fields = [
            'conversation',
            'sender',
            'message_body',
            'attachments',
        ]
        
        read_only_field= ['message_body']
        
    
    def get_queryset(self , obj):
        return Message.objects.select_related('conversation').get().order_by('-timestamp')#conversation_id=obj.conversation_id