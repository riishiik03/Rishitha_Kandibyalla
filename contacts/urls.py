from django.urls import path
from . import views


urlpatterns = [
    path('', views.contacts_list, name='contacts_list'),
    path('contact/', views.contacts_form, name='contacts_form'),
    path('contact/create/', views.contacts_form, name='contacts_create'),
    path('contact/<int:id>/', views.contacts_detail, name='contacts_detail'),
]