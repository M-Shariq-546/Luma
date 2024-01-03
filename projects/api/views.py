from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import( RetrieveAPIView, ListAPIView, CreateAPIView,
                                    UpdateAPIView, 
                                    DestroyAPIView,
                                    CreateAPIView,)
from .serializers import (ProjectSerializer, TasksListSerializer ,
                          createProjectSerializer,
                          UpdateTaskSerilaizer)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        )
from .permissions import IsOwnerOrReadOnly
from projects.models import Project ,Task

class CreateProjectsApiView(CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(is_active=True)

class CreateTaskApiView(CreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TasksListSerializer
    queryset = Project.objects.filter(is_active=True)
    lookup_field = 'project_id'

    def post(self, request, *args,**kwargs):
        project = Project.objects.get(project_id=self.kwargs['project_id'])
        name = request.data.get('name')
        status = request.data.get("status")
        task = Task.objects.create(director=project.owner, project_id=project , name=name , status=status)
        task.save()
        return Response({"Success Message":"Task SuccessFully Created"})


class ProjectsListApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(is_active=True)

class ProjectsCreateApiView(CreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = createProjectSerializer
    queryset = Project.objects.filter(is_active=True)


class TaskListApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TasksListSerializer
    lookup_field = 'project_id'
    queryset = Task.objects.filter(Q(is_active=True))
    
    def get_queryset(self):
        return Task.objects.filter(project_id__project_id=self.kwargs['project_id']).select_related('project_id')

class UpdateTaskApiView(RetrieveAPIView, UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateTaskSerilaizer
    queryset = Task.objects.filter(is_active=True)
    lookup_field = 'name'        
        
class ProjectsDetailApiView(ListAPIView , UpdateAPIView, DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(is_active=True)
    lookup_field = 'project_id'
    
    def get_queryset(self):
        return Project.objects.filter(Q(project_id=self.kwargs['project_id']) & Q(is_active=True)) 
        
    def destroy(self, request , *args , **kwargs):
        instance = self.get_object()
        print(instance)
        instance.is_active = False
        instance.save()
        return Response({"Project Status": "Successfully Delete the Project"}, status=status.HTTP_201_CREATED)