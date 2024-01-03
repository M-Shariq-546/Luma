from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView, 
                                     RetrieveAPIView,
                                     CreateAPIView)
from rest_framework.permissions import (
                                    IsAuthenticated
)
from rest_framework.parsers import MultiPartParser
from .serializers import (MessageSerializer,
                          MessageInboxSerializer,
                          ConverstaionSerializers,
                          CreateConverstaionSerializers)
from chatroom.models import Message , Conversation

class CreateConversationApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateConverstaionSerializers
    queryset = Conversation.objects.filter(is_active=True)
    
    def post(self , request , *args , **kwargs):
        return self.create(request , *args , **kwargs)


class CoversationListApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConverstaionSerializers
    queryset = Conversation.objects.filter(is_active=True)


class MessageListApiView(ListAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MessageSerializer
    lookup_field = 'chatroom'
    queryset = Message.objects.all()
    
    def get_queryset(self):
        return Message.objects.filter(conversation__chatroom=self.kwargs.get('chatroom'))
        
    
class MessageInboxApiView(RetrieveAPIView, CreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MessageInboxSerializer
    queryset = Message.objects.all()
    parser_classes = [MultiPartParser]
    lookup_field = 'chatroom'
    
    def get(self, request, *args, **kwargs):
        try:
            last_message = Message.objects.filter(conversation__chatroom=self.kwargs['chatroom']).latest('timestamp')
            last_message_sender = last_message.sender.user.username
            last_message_body = last_message.message_body
            last_message_image = last_message.profile_image.url
        except Message.DoesNotExist:
            last_message_body = "No messages yet."
            last_message_sender = "You can initiate This Conversation."
            last_message_image = "Your Profile Image Would be shown here"
        return Response({"LastMessage": last_message_body, "sender":last_message_sender, "profile_image":last_message_image}, status=status.HTTP_200_OK)