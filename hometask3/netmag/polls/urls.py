from django.urls import path
from django.conf.urls.static import static
from netmag import settings
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:task_id>', views.detail, name='detail'),
    #path('add', views.add, name='add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
