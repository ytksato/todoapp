from django.http import HttpResponse
from django.shortcuts import render

# クラスベースビュー
from django.views.generic.list import ListView
from todoapp.models import Task

# 関数ベースビュー
# def taskList(request):
#     return HttpResponse('Hello World')

# クラスベースビュー
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'