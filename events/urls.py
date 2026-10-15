from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:id>/',views.event_detail, name='event_detail'),
    path('events/create/', views.event_create, name='event_create'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path( 'events/<int:id>/delete/',views.event_confirm_delete,name='event_confirm_delete'),
]
