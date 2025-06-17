from django.urls import path, include
from glam_ai.views import *
urlpatterns = [
    path('showroom/', include('showRoom.urls')),
    path('db/', include('db.urls')),
    path('glam/', get_data, name='data'),

]
