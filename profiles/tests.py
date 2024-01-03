from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Profile

class userTesting(TestCase):
    def setUp(self):
        user = user = User.objects.create(username='msdevs', first_name="MSDevs", email='msdevs@hotmail.com')
        user.set_password('msdevs.11')
        user.save()
        
    def test_Profile_creation(self):
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user,group_name='MSGroup')
        self.assertEqual(new_profile.id , 1)
        qs = Profile.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Profile Creation Unit Test Passed")
        
    def test_Profile_updation(self):
        user = User.objects.get(username='msdevs')
        profile = Profile.objects.create(user=user,group_name='MSGroup')
        new_profile = Profile.objects.update(user=user, group_name='MSCreation')
        self.assertEqual(new_profile , 1)
        qs = Profile.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Profile Updation Unit Test Passed")
        
    def test_Profile_Deletion(self):
        user = User.objects.get(username='msdevs')
        profile = Profile.objects.create(user=user,group_name='MSGroup')
        profile.is_active = False
        profile.save()
        self.assertEqual(profile.id , 1)
        qs = Profile.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Profile Deletion Unit Test Passed")