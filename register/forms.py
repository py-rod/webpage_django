from django import forms
from django.forms import ModelForm
from .models import Task


class NewUser(forms.Form):
    user = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control" , "placeholder" :"write a title"}),
            "description": forms.Textarea(attrs={"class": "form-control" , "placeholder" :"write description"}),
            "important" : forms.CheckboxInput(attrs={"class": "form-check-input m-auto"})
        }
