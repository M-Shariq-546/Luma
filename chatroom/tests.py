from django.test import TestCase
from .models import Conversation
from django.contrib.auth.models import User
from profiles.models import Profile

class ChatRoomUnitTesting(TestCase):
    def setUp(self):
        user = user = User.objects.create(username='msdevs', first_name="MSDevs", email='msdevs@hotmail.com')
        user.set_password('msdevs.11')
        user.save()
        
    def test_create_chatroom(self):
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user)
        new_chatroom = Conversation.objects.create(chatroom_name="Testing Chatroom", sender=new_profile, receiver=new_profile)
        self.assertEqual(new_chatroom.sender_id , 1)
        qs = Conversation.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Conversation Creation Unit Testing Passed")
        
    