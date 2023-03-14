from django.urls import path
from staff.views import inicio, index

urlpatterns = [
    path('', inicio),
    path('index/', index)
]
