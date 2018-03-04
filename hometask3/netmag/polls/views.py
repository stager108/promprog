from django.shortcuts import render
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    latest_question_list = Task.objects.order_by('-date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

"""
def index2(request):
    latest_question_list = Task.objects.order_by('-date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def latest(request):
    latest_question_list = Task.objects.order_by('-date')[:5]
    output = ', '.join([q.tasktext for q in latest_question_list])
    return HttpResponse(output)
"""
def detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'polls/detail.html', {'task': task})


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_ready = False
            instance.is_imp = False
            instance.save()
            return HttpResponseRedirect('')

        else:
            print(form.errors)
    else:
        form = TaskForm()
    context_dict = dict()
    context_dict['task_form'] = form
    return render(request, 'polls/add.html', context_dict)
