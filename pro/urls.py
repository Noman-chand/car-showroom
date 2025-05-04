from django.urls import path, include

urlpatterns = [
    path('showroom/', include('showRoom.urls')),
    path('db/', include('db.urls')),
]
