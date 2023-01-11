from django.urls import path
from election_poll_app import views 
urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('get-summed-poll/', views.get_poll_result, name='summed_poll')
]