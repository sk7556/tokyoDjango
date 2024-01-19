
from django.contrib import admin
from django.urls import path
from toDo import views as toDo_views

urlpatterns = [
    path('', toDo_views.index, name="toDo_index"),
    path('admin/', admin.site.urls),
]
