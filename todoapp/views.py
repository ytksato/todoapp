from django.http import HttpResponse
from django.shortcuts import render

# クラスベースビュー
from django.views.generic.list import ListView
from todoapp.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

# Taskの作成ページ
class TaskCreate(CreateView):
    model = Task
    # カラムを全部指定
    fields = '__all__'
    # 登録が終わった遷移先を指定
    success_url = reverse_lazy('task-list')

# Taskの更新ページ
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

# Taskの削除ページ
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')