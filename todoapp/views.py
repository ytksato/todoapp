from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render

# クラスベースビュー
from django.views.generic.list import ListView
from todoapp.models import Task
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# 認証周り
from django.contrib.auth.views import LoginView

# ログインしていないと見れないようにする
from django.contrib.auth.mixins import LoginRequiredMixin

# user新規登録
from django.contrib.auth.forms import UserCreationForm
# ログイン後の遷移先
from django.contrib.auth import login


# 関数ベースビュー
# def taskList(request):
#     return HttpResponse('Hello World')

# クラスベースビュー
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # テンプレートで使う変数名を指定
    context_object_name = 'tasks'

    # フィルターをかける
    # ListViewが持ってるメソッドをオーバーライドしている
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # contextを上書きもできる
        context['test'] = 'testcontext'

        # ログインしているユーザーのみ表示
        # context['tasks']の中身にmodelのuserを利用してログインユーザー（self.request.user）でフィルターをかける
        # テンプレートで使う変数名である「tasks」を上書きしている
        context['tasks'] = context['tasks'].filter(user=self.request.user) or ''

        # 検索
        searchInputText = self.request.GET.get('search')
        #print(searchInputText)
        if searchInputText:
            #context['tasks'] = context['tasks'].filter(title__startswith=searchInputText)
            context['tasks'] = context['tasks'].filter(title__icontains=searchInputText)

        # 検索ボックスに入力した文字を保持
        context['search'] = searchInputText
        #print(context)

        return context

# Taskの詳細ページ
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

# Taskの作成ページ
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # カラムを全部指定
    #fields = '__all__'
    fields = ['title', 'description', 'completed']
    # 登録が終わった遷移先を指定
    success_url = reverse_lazy('task-list')

    # タスク作成時にログインユーザーを指定
    def form_valid(self, form):
        # ログインユーザーを取得
        form.instance.user = self.request.user
        return super().form_valid(form)

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
    
# ユーザー登録
class RegisterTodoApp(FormView):
    template_name = 'todoapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')

    # フォームのバリデーションが成功したら実行
    def form_valid(self, form):
        # ユーザーを作成
        user = form.save()
        # ユーザーをログインさせる
        if user is not None:
            login(self.request, user)

        return super().form_valid(form)

    # ログインしている場合はホーム画面にリダイレクト
    def get(self, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return HttpResponse('ログインしています')
        return super().get(*args, **kwargs)