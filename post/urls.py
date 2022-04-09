from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createpost/', views.createpost, name='createpost'),
#    path('single_post/<int:pk>/', views.single_post, name='single_post'),
]