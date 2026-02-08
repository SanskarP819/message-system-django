"""
Admin Panel Configuration - View and manage data in Django Admin
"""
from django.contrib import admin
from .models import EmailLog, SmsLog, WhatsAppLog


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    """Email Log Admin"""
    list_display = ('id', 'email_to', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('email_to',)
    ordering = ('-timestamp',)


@admin.register(SmsLog)
class SmsLogAdmin(admin.ModelAdmin):
    """SMS Log Admin"""
    list_display = ('id', 'mobile_number', 'message', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('mobile_number', 'message')
    ordering = ('-timestamp',)


@admin.register(WhatsAppLog)
class WhatsAppLogAdmin(admin.ModelAdmin):
    """WhatsApp Log Admin"""
    list_display = ('id', 'mobile_number', 'message', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('mobile_number', 'message')
    ordering = ('-timestamp',)