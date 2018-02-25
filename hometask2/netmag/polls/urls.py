from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:task_id>', views.detail, name='detail'),
    path('add', views.add, name='add'),
]
