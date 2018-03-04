from django.contrib.auth.models import User, Group
from rest_framework import serializers
from polls.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'taskname', 'tasktext', 'date', 'is_imp', 'is_ready')
