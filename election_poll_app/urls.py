from django.urls import path
from election_poll_app import views 
urlpatterns = [
    path('home/', views.homepage, name='hompage'),
]