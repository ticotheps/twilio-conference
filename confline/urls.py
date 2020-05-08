from django.urls import path

from .views import my_conference_line

urlpatterns = [
    path('', my_conference_line, name='my_conference_line'),
]