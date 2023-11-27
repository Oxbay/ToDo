from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm
from manager.models import Task, Tag


class TaskList(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 10


class TaskCreate(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")


class TagList(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreate(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("manager:tag-list")


class TagUpdate(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("manager:tag-list")


class TagDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("manager:tag-list")


def task_status(request, pk: int):
    task = Task.objects.get(pk=pk)

    if task.status:
        task.status = False
    else:
        task.status = True

    task.save()

    return HttpResponseRedirect(reverse_lazy("manager:task-list"))
