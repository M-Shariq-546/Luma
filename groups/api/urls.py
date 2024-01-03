from django.contrib import admin
from django.urls import path, include
from .views import (
                    CreateGroupApiView,
                    GroupInviteApiView,
                 DetailGroupApiView,
                 ListGroupApiView,
                 DetailGroupUpdateApiView,
                 RemoveMemberApiView)
urlpatterns = [
    path('create-group/', CreateGroupApiView.as_view()),
    path('invite/', GroupInviteApiView.as_view()),
    path('', ListGroupApiView.as_view()),
    path('<str:group_id>/', DetailGroupApiView.as_view()),
    path('<str:group_id>/update', DetailGroupUpdateApiView.as_view()),
    path('<str:group_id>/members/remove_member/<int:member>/', RemoveMemberApiView.as_view()),    
]
