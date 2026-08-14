from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Todo import views as todo_views
from User import views as user_views

router = DefaultRouter()
router.register(r'todos', todo_views.TodoViewSet, basename='todos')
router.register(r'users', user_views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
