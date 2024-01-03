from django.urls import path, include
from .views import (UserProfileApiView,
                    AllProfileApiView,
                    ProfileDeleteApiView , 
                    ProfileUpdateApiView,
                    CreateUserApiView,
                    CreateProfileApiView
                    )
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('profiles/', AllProfileApiView.as_view()),
    path('profile/<str:profile>/', UserProfileApiView.as_view()),
    path('user-creation/', CreateUserApiView.as_view()),
    path('create-profile/', CreateProfileApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('profile/<str:profile>/delete/', ProfileDeleteApiView.as_view()),
    path('profile/<str:profile>/update/', ProfileUpdateApiView.as_view()),    
]
