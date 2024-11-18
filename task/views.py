
from django.utils import timezone
from .models import Tasks
from django.views.generic import (ListView,UpdateView)
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import TaskForm

class TasksListView(ListView):
    model = Tasks
    template_name ='tasks/list_tasks.html'
    context_object_name = 'tasks'
    
class AddTaskView(FormView):
    template_name = 'tasks/add_task.html'  # Optional: if you want a separate template
    form_class = TaskForm
    success_url = reverse_lazy('task_list')  # Redirect to the task list after successful submission

    def form_valid(self, form):
        # Save the task with default status as 'Pending'
        form.instance.status = 'Pending'
        form.save()
        return super().form_valid(form)
    
    
class TaskUpdateView(UpdateView):
    model = Tasks
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.updated = timezone.now()
        return super().form_valid(form)
