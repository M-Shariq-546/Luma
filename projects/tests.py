from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Project, Task
from profiles.models import Profile

class userTesting(TestCase):
    def setUp(self):
        user = User.objects.create(username='msdevs', first_name="MSDevs", email='msdevs@hotmail.com')
        user.set_password('msdevs.11')
        user.save()
        
    def test_Project_creation(self): 
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user,group_name='MSGroup')
        self.assertEqual(new_profile.id , 1)
        qs = Profile.objects.all()
        self.assertEqual(qs.count() , 1)      
        new_project = Project.objects.create(owner=new_profile.user, project_name="Testing 123..." , assigned_to=new_profile.user)
        self.assertEqual(new_project.id , 1)
        qs = Project.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Project Creation Unit Test Passed")
        
    def test_Project_Updation(self): 
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user,group_name='MSGroup')
        self.assertEqual(new_profile.id , 1)
        qs = Profile.objects.all()
        self.assertEqual(qs.count() , 1)      
        new_project = Project.objects.create(owner=new_profile.user, project_name="Testing 123..." , assigned_to=new_profile.user)
        self.assertEqual(new_project.id , 1)
        qs = Project.objects.all()
        self.assertEqual(qs.count() , 1)
        new_project_update = Project.objects.update(owner=new_profile.user, project_name="Testing Updation" , assigned_to=new_profile.user)
        self.assertEqual(new_project_update , 1)
        qs = Project.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Project Updation Unit Test Passed")
        
    def test_Project_Deletion(self): 
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user,group_name='MSGroup')
        self.assertEqual(new_profile.id , 1)
        qs = Profile.objects.all()
        self.assertEqual(qs.count() , 1)      
        new_project = Project.objects.create(owner=new_profile.user, project_name="Testing 123..." , assigned_to=new_profile.user)
        self.assertEqual(new_project.id , 1)
        qs = Project.objects.all()
        self.assertEqual(qs.count() , 1)
        project = Project.objects.get(project_name="Testing 123...")
        project.is_active = False
        project.save()
        self.assertEqual(project.id , 1)
        qs = Project.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Project Deletion Unit Test Passed")
        
        
    def test_task_creation(self):
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user,group_name='MSGroup')
        self.assertEqual(new_profile.id , 1)
        qs = Profile.objects.all()
        self.assertEqual(qs.count() , 1)      
        new_project = Project.objects.create(owner=new_profile.user, project_name="Testing 123..." , assigned_to=new_profile.user)
        self.assertEqual(new_project.id , 1)
        qs = Project.objects.all()
        self.assertEqual(qs.count() , 1)
        new_task = Task.objects.create(name="New Test Task", project_id=new_project, director=new_profile.user, status='Assigned')
        self.assertEqual(new_task.id , 1)
        qs = Task.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Task Creation Test Case Passed")
        
    def test_task_updation(self):
        user = User.objects.get(username='msdevs')
        new_profile = Profile.objects.create(user=user,group_name='MSGroup')
        self.assertEqual(new_profile.id , 1)
        qs = Profile.objects.all()
        self.assertEqual(qs.count() , 1)      
        new_project = Project.objects.create(owner=new_profile.user, project_name="Testing 123..." , assigned_to=new_profile.user)
        self.assertEqual(new_project.id , 1)
        qs = Project.objects.all()
        self.assertEqual(qs.count() , 1)
        new_task = Task.objects.create(name="New Test Task", project_id=new_project, director=new_profile.user, status='Assigned')
        self.assertEqual(new_task.id , 1)
        qs = Task.objects.all()
        self.assertEqual(qs.count() , 1)
        new_task_update = Task.objects.update(name="New Test Task", project_id=new_project, director=new_profile.user, status='Completed')
        self.assertEqual(new_task_update , 1)
        qs = Task.objects.all()
        self.assertEqual(qs.count() , 1)
        print("Task Updation Test Case Passed")