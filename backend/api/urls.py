"""
API URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    # Email endpoints
    path('email/send', views.send_email, name='send_email'),
    path('email/list', views.get_all_emails, name='get_all_emails'),
    
    # SMS endpoints
    path('sms/send', views.send_sms, name='send_sms'),
    path('sms/list', views.get_all_sms, name='get_all_sms'),
    
    # WhatsApp endpoints
    path('whatsapp/send', views.send_whatsapp, name='send_whatsapp'),
    path('whatsapp/list', views.get_all_whatsapp, name='get_all_whatsapp'),
]