from django.http import HttpResponse
from django.shortcuts import render

# クラスベースビュー
from django.views.generic.list import ListView
from todoapp.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# 認証周り
from django.contrib.auth.views import LoginView

# ログインしていないと見れないようにする
from django.contrib.auth.mixins import LoginRequiredMixin

# 関数ベースビュー
# def taskList(request):
#     return HttpResponse('Hello World')

# クラスベースビュー
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # テンプレートで使う変数名を指定
    context_object_name = 'tasks'

# Taskの詳細ページ
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

# Taskの作成ページ
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # カラムを全部指定
    fields = '__all__'
    # 登録が終わった遷移先を指定
    success_url = reverse_lazy('task-list')

# Taskの更新ページ
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

# Taskの削除ページ
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')

# 認証周り
class TaskListLoginView(LoginView):
    # デフォルトのテンプレート名はregistration/login.html
    template_name = 'todoapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')