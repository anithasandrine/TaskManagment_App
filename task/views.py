
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from .models import Tasks
from django.views.generic import (ListView, UpdateView, DetailView, DeleteView,View)
from django.views.generic.edit import FormView
from django.urls import reverse_lazy,reverse
from .forms import TaskForm
from django.contrib import messages
class TasksListView(ListView):
    model = Tasks
    template_name = 'tasks/list_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter tasks by the logged-in user
        queryset = queryset.filter(owner=self.request.user)
        
        # Implement search and filter
        query = self.request.GET.get('q')
        status_filter = self.request.GET.get('status')

        if query:
            queryset = queryset.filter(title__icontains=query)
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        return queryset

    
class AddTaskView(FormView):
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        # Assign the logged-in user as the owner
        form.instance.owner = self.request.user
        form.instance.status = 'Pending'
        form.save()

        # Add a success message
        messages.success(self.request, f"Task '{form.instance.title}' was successfully added.")
        return super().form_valid(form)
    
    
class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        # Restrict access to the owner
        return super().get_queryset().filter(owner=self.request.user)

class TaskUpdateView(UpdateView):
    model = Tasks
    fields = ['title', 'description', 'status']
    template_name = 'tasks/update_task.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        # Restrict updates to the owner
        return super().get_queryset().filter(owner=self.request.user)

    def form_valid(self, form):
        form.instance.updated = timezone.now()
        response = super().form_valid(form)
        messages.success(self.request, f"Task '{form.instance.title}' was successfully updated.")
        return response


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/confirm_delete.html'
    success_url = reverse_lazy('task_list')
    success_message = "Task was successfully deleted."

    def get_queryset(self):
        # Restrict deletion to the owner
        return super().get_queryset().filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
    
class TaskStatusUpdateView(View):
    def get(self, request, pk):
        task = Tasks.objects.filter(pk=pk, owner=request.user).first()
        if task:
            task.status = 'Completed'
            task.save()
            messages.success(request, f"Task '{task.title}' status updated to Completed.")
        else:
            messages.error(request, "You do not have permission to update this task.")
        return HttpResponseRedirect(reverse('task_list'))
