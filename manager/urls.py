from django.urls import path

from manager.views import (
    TaskList,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    TagList,
    TagCreate,
    TagUpdate,
    TagDelete,
    task_status,
)

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("task/create/", TaskCreate.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdate.as_view(), name="task-update"),
    path("task/<int:pk>/status/", task_status, name="task-status"),
    path("task/<int:pk>/delete/", TaskDelete.as_view(), name="task-delete"),
    path("tags/", TagList.as_view(), name="tag-list"),
    path("tags/create/", TagCreate.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdate.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDelete.as_view(), name="tag-delete"),
]


app_name = "manager"
