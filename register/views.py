from django.shortcuts import render, redirect
from .forms import NewUser, CreateTaskForm
from .models import DataUser1, DataUser2, Task
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


# Metodo video
def home(request):
    return render(request, "home.html")


def signup(request):
    # obteniendo datos y mostrando en la pagina
    if request.method == "GET":
        return render(
            request,
            "signup.html",
            {"form": UserCreationForm},
        )
    else:
        # comprobando si las dos contraseña coinciden antes de hacer el guardado
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # registrando usuario
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                # guardando usuario nuevo
                user.save()
                return redirect("login")
            except IntegrityError:
                # mostrando en pantalla si el usuario existe en la base de datos
                return render(
                    request,
                    "signup.html",
                    {
                        "form": UserCreationForm,
                        "error": "Existing user",
                    },
                )
        else:
            # si no las contraseña no coinciden me mostrara el mensaje de error
            return render(
                request,
                "signup.html",
                {
                    "form": UserCreationForm,
                    "error": "Password don't match",
                },
            )


@login_required(login_url="login")
def task(request):
    # mostrando tareas por medio del filtrado de id de la cuenta logueada
    task = Task.objects.filter(user=request.user)
    return render(request, "task.html", {"tasks": task})


def loginsession(request):
    # obteniendo tarea y mostrandola en pantalla
    if request.method == "GET":
        return render(
            request,
            "login.html",
            {
                "form": AuthenticationForm,
            },
        )
    else:
        # verificando si el username y la contraseña son correctas
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        # si el usuario y la contraseña estan vacias me mostrara ese mensaje de error
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username or Password is incorrect",
                },
            )
        else:
            # si todo esta bien me redireccionara a la pagina de tareas
            login(request, user)
            return redirect("task")

        return render(
            request,
            "login.html",
            {
                "form": AuthenticationForm,
            },
        )


def closesession(request):
    # cargando logout de la sesion
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def create_task(request):
    # obteniendo tarea y mostrandola en pantalla
    if request.method == "GET":
        return render(
            request,
            "create_task.html",
            {
                "form": CreateTaskForm,
            },
        )
    else:
        # guardando nueva tarea
        try:
            form = CreateTaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("task")
        except ValueError:
            return render(
                request,
                "create_task.html",
                {
                    "form": CreateTaskForm,
                    "error": "Put data value",
                },
            )


@login_required(login_url="login")
def task_detail(request, task_id):
    # obteniendo tarea y mostrandola en pantalla
    if request.method == "GET":
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = CreateTaskForm(instance=task)
        return render(
            request,
            "task_detail.html",
            {
                "task": task,
                "form": form,
            },
        )
    else:
        try:
            # actualizando cambios de la tarea seleccionada
            taskupdate = get_object_or_404(Task, pk=task_id, user=request.user)
            form = CreateTaskForm(request.POST, instance=taskupdate)
            form.save()
            return redirect("task")
        except ValueError:
            return render(
                request,
                "task_detail.html",
                {
                    "form": form,
                    "error": "Error updating task",
                },
            )


@login_required(login_url="login")
def task_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.datecomplete = timezone.now()
        task.save()
        return redirect("task")
        return render(request, "task.html", {"task": task})


@login_required(login_url="login")
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("task")


# # Metodo personal
# def create_user(request):
#     if request.method == "GET":
#         return render(request, "register.html", {"form": NewUser()})
#     else:
#         if request.POST["password1"] == request.POST["password2"]:
#             try:
#                 DataUser1.objects.create(
#                     user=request.POST["user"],
#                     email=request.POST["email"],
#                     password1=request.POST["password1"],
#                 )
#                 return redirect("task.html")
#             except:
#                 return render(request, "register.html", {
#                     "form": NewUser(),
#                     "error": "Existing user", })
#         else:
#             return render(request, "register.html", {
#                 "form": NewUser(),
#                 "error": "Password don't match",
#             })
