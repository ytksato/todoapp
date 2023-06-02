from django.urls import path
from . import views
from .views import TaskList, TaskDetail

urlpatterns = [
    # 関数ベースビューの書き方
    #path('', views.taskList),

    # クラスベースビューの書き方
    path('', TaskList.as_view()),
    # <int:pk>でidを取得(動的キー)
    path('task/detail/<int:pk>', TaskDetail.as_view(), name='task-detail'),
]
