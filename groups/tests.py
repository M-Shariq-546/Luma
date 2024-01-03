from django.test import TestCase
from profiles.models import Profile
from projects.models import Project, Task
from .models import Group , Members
from django.contrib.auth.models import User

class GroupUnitTesting(TestCase):
    def setUp(self):
        user = user = User.objects.create(username='msdevs', first_name="MSDevs", email='msdevs@hotmail.com')
        user.set_password('msdevs.11')
        user.save()
        
    def test_group_creation(self):
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user)
        group = Group.objects.create(admin=new_profile, group_name="MSDEVS")
        self.assertEqual(group.id , 1)
        qs = Group.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Group Creation Unit Testing Passed")
        
    def test_group_updation(self):
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user)
        group = Group.objects.create(admin=new_profile, group_name="MSDEVS")
        self.assertEqual(group.id , 1)
        group = Group.objects.update(admin=new_profile, group_name="Shariq's group")
        self.assertEqual(group , 1)
        qs = Group.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Group Updation Unit Testing Passed") 

    def test_invite_member(self):
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user)
        member = Members.objects.create(member=new_profile)
        member.is_invited = True
        member.save()
        self.assertEqual(member.id , 1)
        qs = Members.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Member Invitation Unit Testing Passed")

    def test_remove_member(self):
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user)
        member = Members.objects.create(member=new_profile)
        get_member = Members.objects.get(member=new_profile)
        get_member.is_active = False
        get_member.save()
        self.assertEqual(get_member.id , 1)
        qs = Members.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Member Removing Test Case Passed ")