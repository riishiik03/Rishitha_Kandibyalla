from django.urls import path
from . import views


urlpatterns = [
    path('', views.contacts_list, name='contacts_list'),
    path('contact/', views.contacts_form, name='contacts_form'),
    path('contact/create/', views.contacts_create, name='contacts_create'),
    path('contact/<int:id>/', views.contacts_detail, name='contacts_detail'),
    path('edit_contact/<int:contact_id>/', views.contacts_update, name='contacts_update'),
    path('contacts/<int:contact_id>/confirm_delete/', views.contacts_confirm_delete, name='contacts_confirm_delete'),
]

    #path('contacts/<int:contact_id>/confirm_delete/', views.contacts_confirm_delete, name='contacts_confirm_delete'),
    


