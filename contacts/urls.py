from django.urls import path
from . import views


urlpatterns = [
    path('', views.contacts_list, name='contacts_list'),
    path('contact/', views.contacts_new, name='contacts_form'),
    path('contact/<int:id>/', views.contacts_detail, name='contacts_detail'),
    path('contact/<int:id>/edit/', views.contacts_edit, name='contacts_update'),
    path('contact/<int:id>/delete/', views.contacts_delete, name='contacts__confirm_delete'),
]