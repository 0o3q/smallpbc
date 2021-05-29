from django.urls import path, include
from .views import BoardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('boards', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
