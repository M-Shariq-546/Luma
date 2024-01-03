from django.urls import path, include
from .views import (ProjectsListApiView,
                    ProjectsDetailApiView,
                    TaskListApiView,
                    CreateTaskApiView,
                    ProjectsCreateApiView,
                    UpdateTaskApiView,
                    )

urlpatterns = [
    path('create_project/', ProjectsCreateApiView.as_view()),
    path('<str:project_id>/create_task/', CreateTaskApiView.as_view()), 
    path('list/', ProjectsListApiView.as_view()),
    path('<str:project_id>/tasks_list/', TaskListApiView.as_view()),
    path('<str:project_id>/tasks_list/<str:name>/', UpdateTaskApiView.as_view()),
    path('<str:project_id>/', ProjectsDetailApiView.as_view()),      
]
