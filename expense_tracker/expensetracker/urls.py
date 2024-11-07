from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AdminViewSet, TransactionViewSet, LogViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'logs', LogViewSet)

urlpatterns =[
    path('',include(router.urls))
]