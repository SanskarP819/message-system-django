"""
Serializers - Convert between Python objects and JSON (Similar to DTOs)
"""
from rest_framework import serializers
from .models import EmailLog, SmsLog, WhatsAppLog
from django.core.validators import EmailValidator, RegexValidator


# ============ REQUEST SERIALIZERS ============

class EmailRequestSerializer(serializers.Serializer):
    """
    Email Request Serializer - validates incoming email data
    """
    emailTo = serializers.EmailField(
        required=True,
        error_messages={
            'required': 'Email is required',
            'invalid': 'Email should be valid'
        }
    )
    
    def validate_emailTo(self, value):
        """Custom validation for email"""
        if not value:
            raise serializers.ValidationError("Email is required")
        return value


class SmsRequestSerializer(serializers.Serializer):
    """
    SMS Request Serializer - validates incoming SMS data
    """
    mobileNumber = serializers.CharField(
        required=True,
        max_length=10,
        error_messages={
            'required': 'Mobile number is required'
        }
    )
    message = serializers.CharField(
        required=True,
        error_messages={
            'required': 'Message is required'
        }
    )
    
    def validate_mobileNumber(self, value):
        """Validate mobile number is 10 digits"""
        if not value:
            raise serializers.ValidationError("Mobile number is required")
        if not value.isdigit():
            raise serializers.ValidationError("Mobile number must contain only digits")
        if len(value) != 10:
            raise serializers.ValidationError("Mobile number must be 10 digits")
        return value
    
    def validate_message(self, value):
        """Validate message is not empty"""
        if not value or not value.strip():
            raise serializers.ValidationError("Message is required")
        return value


class WhatsAppRequestSerializer(serializers.Serializer):
    """
    WhatsApp Request Serializer - validates incoming WhatsApp data
    """
    mobileNumber = serializers.CharField(
        required=True,
        max_length=10,
        error_messages={
            'required': 'Mobile number is required'
        }
    )
    message = serializers.CharField(
        required=True,
        error_messages={
            'required': 'Message is required'
        }
    )
    
    def validate_mobileNumber(self, value):
        """Validate mobile number is 10 digits"""
        if not value:
            raise serializers.ValidationError("Mobile number is required")
        if not value.isdigit():
            raise serializers.ValidationError("Mobile number must contain only digits")
        if len(value) != 10:
            raise serializers.ValidationError("Mobile number must be 10 digits")
        return value
    
    def validate_message(self, value):
        """Validate message is not empty"""
        if not value or not value.strip():
            raise serializers.ValidationError("Message is required")
        return value


# ============ RESPONSE SERIALIZERS ============

class EmailResponseSerializer(serializers.ModelSerializer):
    """
    Email Response Serializer - formats email data for response
    """
    emailTo = serializers.EmailField(source='email_to')
    
    class Meta:
        model = EmailLog
        fields = ['id', 'emailTo', 'timestamp']


class SmsResponseSerializer(serializers.ModelSerializer):
    """
    SMS Response Serializer - formats SMS data for response
    """
    mobileNumber = serializers.CharField(source='mobile_number')
    
    class Meta:
        model = SmsLog
        fields = ['id', 'mobileNumber', 'message', 'timestamp']


class WhatsAppResponseSerializer(serializers.ModelSerializer):
    """
    WhatsApp Response Serializer - formats WhatsApp data for response
    """
    mobileNumber = serializers.CharField(source='mobile_number')
    
    class Meta:
        model = WhatsAppLog
        fields = ['id', 'mobileNumber', 'message', 'timestamp']