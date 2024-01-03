from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import( RetrieveAPIView, ListAPIView, CreateAPIView,
                                    UpdateAPIView, 
                                    DestroyAPIView,
                                    CreateAPIView,)
from .serializers import (ProfileSerializer, 
                          ProfileUpdateSerializer,
                          UserCreationSerializer,
                          CreateProfileSerializer)
from profiles.models import Profile
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticatedOrReadOnly
                                        )
from .permissions import IsOwnerOrReadOnly

class CreateUserApiView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreationSerializer
    queryset = Profile.objects.filter(is_active=True)

    def get_object(self):
        return self.request.user
    
class CreateProfileApiView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateProfileSerializer
    queryset = Profile.objects.filter(is_active=True)

    def get_object(self):
        return self.request.user

class AllProfileApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.filter(is_active=True)

class UserProfileApiView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.filter(is_active=True)
    lookup_field = 'profile'

        
class ProfileUpdateApiView(UpdateAPIView, RetrieveAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.filter(is_active=True)
    lookup_field = 'profile'
    
    def put(self , request,*args, **kwarsg):
        Profile.objects.get(profile=self.kwargs['profile'])
        return self.update(request,*args, **kwarsg)        
        
class ProfileDeleteApiView(DestroyAPIView,RetrieveAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.filter(is_active=True)
    lookup_field = 'profile'
    
    def put(self , request , *args ,**kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self , request , *args ,**kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request , *args , **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response({"Delete Status": "Successfully Delete the profile"}, status=status.HTTP_201_CREATED)