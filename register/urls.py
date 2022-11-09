from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("task/", views.task, name="task"),
    path("task/task_detail/<int:task_id>/", views.task_detail, name="task_detail"),
    path(
        "task/task_detail/<int:task_id>/complete/",
        views.task_complete,
        name="task_complete",
    ),
    path(
        "task/task_detail/<int:task_id>/delete/",
        views.task_delete,
        name="task_delete",
    ),
    path("task/create/", views.create_task, name="create_task"),
    path("login/", views.loginsession, name="login"),
    path("logout/", views.closesession, name="logout")
    # path("register/", views.create_user, name="register"),
]
