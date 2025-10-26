from rest_framework import routers
from .views import TodoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]
