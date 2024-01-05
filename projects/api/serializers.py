from django.db import transaction
from rest_framework import serializers
from projects.models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField(read_only=True)
    director = serializers.SerializerMethodField(read_only=True)
    assigned_to = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Project
        fields = [
            'director',
            'project_id',
            'project_name',
            'assigned_to',
            'due_date',
            'tasks',
        ]
        read_only_field =['project_id']
    
    def get_queryset(self, obj):
        return Project.objects.filter(is_active=True)
    
    def get_assigned_to(self , obj):
        if obj.assigned_to is not None:
            return obj.assigned_to.username
        return ""
    
    def get_director(self , obj):
        if obj.director is not None:
            return obj.director.user.username
        return ""
    
    def get_tasks(self , obj):
        tasks = Project.objects.prefetch_related('tasks').filter(project_id=obj.project_id)
        return str(list(tasks.values('tasks__name')))
        
class createProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'director',
            'project_name',
            'assigned_to',
            'due_date',
        ]
    
    def get_director(self , obj):
        if obj is not None:
            Project.objects.create(director=obj.director)
            return obj.director
        raise ValueError("Director name is required please check Your profiles")
    
    
    def create(self , data):
        project = Project.objects.create(
            director=data.get('director'),
            project_name=data.get("project_name"),
            assigned_to=data.get("assigned_to"),
            due_date = data.get('due_date')
        )
        return project
        
class TasksListSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Task
        fields = [
            'director',
            'name',
            'due_date',
            'status'
        ]
        read_only_field =['director']    
       
    def get_director(self , obj):
        if obj.director is not None:
            return obj.director.username
        return ""
    
class UpdateTaskSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'status'
        ]