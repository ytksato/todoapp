from django.contrib import admin
# Taskモデルをインポートする
from todoapp.models import Task

# Register your models here.
# Taskモデルを登録する
admin.site.register(Task)