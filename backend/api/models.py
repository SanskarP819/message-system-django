"""
Database Models (Similar to JPA Entities)
"""
from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class EmailLog(models.Model):
    """
    Email Log Model - stores email sending records
    """
    email_to = models.EmailField(
        max_length=255,
        validators=[EmailValidator(message="Email should be valid")],
        help_text="Recipient email address"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when email was sent"
    )
    
    class Meta:
        db_table = 'email_logs'
        ordering = ['-timestamp']  # Order by timestamp descending
        verbose_name = 'Email Log'
        verbose_name_plural = 'Email Logs'
    
    def __str__(self):
        return f"Email to {self.email_to} at {self.timestamp}"


class SmsLog(models.Model):
    """
    SMS Log Model - stores SMS sending records
    """
    mobile_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{10}$',
                message='Mobile number must be 10 digits'
            )
        ],
        help_text="10-digit mobile number"
    )
    message = models.TextField(
        max_length=1000,
        help_text="SMS message content"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when SMS was sent"
    )
    
    class Meta:
        db_table = 'sms_logs'
        ordering = ['-timestamp']
        verbose_name = 'SMS Log'
        verbose_name_plural = 'SMS Logs'
    
    def __str__(self):
        return f"SMS to {self.mobile_number} at {self.timestamp}"


class WhatsAppLog(models.Model):
    """
    WhatsApp Log Model - stores WhatsApp message records
    """
    mobile_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{10}$',
                message='Mobile number must be 10 digits'
            )
        ],
        help_text="10-digit mobile number"
    )
    message = models.TextField(
        max_length=1000,
        help_text="WhatsApp message content"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when WhatsApp message was sent"
    )
    
    class Meta:
        db_table = 'whatsapp_logs'
        ordering = ['-timestamp']
        verbose_name = 'WhatsApp Log'
        verbose_name_plural = 'WhatsApp Logs'
    
    def __str__(self):
        return f"WhatsApp to {self.mobile_number} at {self.timestamp}"