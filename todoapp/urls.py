from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    # 関数ベースビューの書き方
    #path('', views.taskList),

    # クラスベースビューの書き方
    path('', TaskList.as_view(), name='task-list'),
    # <int:pk>でidを取得(動的キー)
    path('task/detail/<int:pk>', TaskDetail.as_view(), name='task-detail'),
    # create
    path('task/create/', TaskCreate.as_view(), name='task-create'),
    # update
    path('task/update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    # delete
    path('task/delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]
