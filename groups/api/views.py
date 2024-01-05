from django.db import transaction
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from profiles.models import Profile
from django.core.mail import send_mail
from rest_framework.generics import(
            CreateAPIView,
            ListAPIView,
            RetrieveAPIView,
            DestroyAPIView,
            UpdateAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from groups.models import Group, Members
from .serializers import( GroupCreationSerailizer,
                        GroupInviteSerializer, GroupDetailSerailizer,
                        GroupDetailUpdateSerailizer, RemoveMemberSerializer
                        )
from rest_framework.response import Response
from rest_framework import status

class GroupInviteApiView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GroupInviteSerializer
    queryset = Members.objects.filter(is_active=True)
    
    
    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        user_email = request.data.get('email', None)
        if not user_email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user_profile = Profile.objects.get(user__email=user_email)
        except Profile.DoesNotExist:
            return Response({'Profile Checking Status': 'Profile not found for the given email'}, status=status.HTTP_404_NOT_FOUND)
        member, created = Members.objects.get_or_create(member=user_profile)
        if not created and member.is_invited:
            return Response({'Profile Checking Status': 'User is already invited'}, status=status.HTTP_400_BAD_REQUEST)
        subject = 'This is Invitation Email for Joining Team Group'
        message = 'Please click here to join group team'
        send_mail(
            subject,
            message,
            "MShariq28022000@gmail.com",
            [user_email],
            fail_silently=False,
        )
        member.is_invited = True
        member.save()
        return Response({"Email Status": "Successfully Sent"}, status=status.HTTP_201_CREATED)


class ListGroupApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GroupDetailSerailizer
    queryset = Group.objects.filter(is_active=True)
    
class DetailGroupUpdateApiView(RetrieveAPIView , UpdateAPIView , DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GroupDetailUpdateSerailizer
    lookup_field = 'group_id'
    queryset = Group.objects.filter(is_active=True)

    def put(self , request , *args , **kwargs):
        return self.update(request , *args , **kwargs)

    def destroy(self , request , *args , **kwargs):
        qs = Group.objects.get(group_id=self.kwargs['group_id'])
        qs.is_active = False
        qs.save()
        return Response({"Group Status": "Successfully Delete the Group"}, status=status.HTTP_410_GONE)

    
class DetailGroupApiView(RetrieveAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GroupDetailSerailizer
    lookup_field = 'group_id'
    queryset = Group.objects.filter(is_active=True) 
    

class CreateGroupApiView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GroupCreationSerailizer
    lookup_field = 'admin'
    queryset =  Group.objects.filter(is_active=True)
    
    @transaction.atomic()    
    def post(self , request , *args, **kwargs):
        return self.create(request , *args, **kwargs)
    
    
class RemoveMemberApiView(RetrieveAPIView,DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RemoveMemberSerializer
    lookup_field = 'member'
    queryset =  Members.objects.filter(is_active=True)
    
    @transaction.atomic()
    def destroy(self , request , *args , **kwargs):
        members = Members.objects.get(member=self.kwargs['member'])
        members.is_active = False
        members.save()
        return Response({"Group Status": "Successfully Delete the Group"}, status=status.HTTP_410_GONE)