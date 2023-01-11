from django.urls import path
from .views import HomeView, DetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', DetailView.as_view(), name='post-details')
]
