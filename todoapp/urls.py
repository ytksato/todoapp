from django.urls import path
from . import views
from .views import TaskList

urlpatterns = [
    # 関数ベースビューの書き方
    #path('', views.taskList),

    # クラスベースビューの書き方
    path('', TaskList.as_view(), name='tasks'),
]
