from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # アプリの方で作ったurls.pyを読み込む
    path('', include('todoapp.urls')),
]
