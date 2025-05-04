from django.urls import path, include
from rest_framework.routers import DefaultRouter
from db.views import CreatePersonView

router = DefaultRouter()
router.register(r'add', CreatePersonView, basename='person')

urlpatterns = [
    path('', include(router.urls)),
]
