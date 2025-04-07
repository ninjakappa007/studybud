from django.urls import path
# importing by views from base.views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("room/<str:pk>/", views.room, name="room"),
]