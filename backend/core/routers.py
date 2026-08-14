

from django.db import router
from rest_framework.routers import DefaultRouter
from backend.User import views


    
router = DefaultRouter() 
router.register(r'todos', views.TodoViewSet, basename='todos') 
router.register(r'users', User.views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),  
]