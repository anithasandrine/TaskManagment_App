from django.urls import path
from . import views
urlpatterns = [
    path('', views.TasksListView.as_view(), name='task_list'),
    path('add-task/', views.AddTaskView.as_view(), name='add_task'),
    path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='update_task'),
]