from django.urls import path
from . import views
urlpatterns = [
    path('', views.TasksListView.as_view(), name='task_list'),
    path('add-task/', views.AddTaskView.as_view(), name='add_task'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/complete/', views.TaskStatusUpdateView.as_view(), name='task_complete'),
]