from django.urls import path
from .views import mainview

urlpatterns = [
    path('', mainview),
]