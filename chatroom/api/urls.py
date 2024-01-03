from django.contrib import admin
from .views import (MessageListApiView,
                    MessageInboxApiView,
                    CoversationListApiView,
                    CreateConversationApiView)
from django.urls import path

urlpatterns = [
      path('create-conversations/', CreateConversationApiView.as_view()),
      path('conversations/', CoversationListApiView.as_view()),
      path('messages/<str:chatroom>/', MessageListApiView.as_view()),
      path('messages/<str:chatroom>/inbox/', MessageInboxApiView.as_view()),
]