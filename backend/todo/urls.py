from django.urls import path
from .views import todo_list, todo_detail

urlpatterns = [
    path('todos/', todo_list.as_view(), name='todo_list'),
    path('todos/<int:pk>/', todo_detail.as_view(), name='todo_detail'),
]
