from django.http import HttpResponse
from django.shortcuts import render

# クラスベースビュー
from django.views.generic.list import ListView
from todoapp.models import Task
from django.views.generic.detail import DetailView

# 関数ベースビュー
# def taskList(request):
#     return HttpResponse('Hello World')

# クラスベースビュー
class TaskList(ListView):
    model = Task
    # テンプレートで使う変数名を指定
    context_object_name = 'tasks'

# Taskの詳細ページ
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'