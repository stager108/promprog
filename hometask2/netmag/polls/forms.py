 
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    taskname = forms.CharField(label="Task name:", required=True, max_length=200)
    tasktext = forms.CharField(label="Description:", required=True, max_length=200)

    class Meta:
        model = Task
        fields = ('taskname', 'tasktext')
