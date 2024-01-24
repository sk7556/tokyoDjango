from django.urls import path
from .views import ToDoAPIView, toDo_page

app_name = 'toDo'

urlpatterns = [
    path('api/todo/', ToDoAPIView.as_view(), name='api_todo'),
    path('', toDo_page, name='toDo_page'),
]
