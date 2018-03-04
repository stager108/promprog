 
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    taskname = forms.CharField(label="Task name:", required=True, max_length=200)
    tasktext = forms.CharField(label="Description:", required=True, max_length=200)
    is_imp = forms.BooleanField(label="Important?", required=True)
    is_ready = forms.BooleanField(label="Done?", required=True)
    

    class Meta:
        model = Task
        fields = ('taskname', 'tasktext', 'is_imp', 'is_ready')
