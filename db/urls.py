# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from db.views import  PersonCreateAPIView
# # from db.views import CreatePersonView , PersonCreateAPIView
#
#
# router = DefaultRouter()
# router.register(r'add', PersonCreateAPIView, basename='person')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from .views import PersonCreateAPIView

urlpatterns = [
    path('persons/', PersonCreateAPIView.as_view(), name='person-list-create'),
]
