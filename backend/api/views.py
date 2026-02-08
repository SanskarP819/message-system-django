"""
Views - Handle HTTP requests and responses (Similar to Controllers + Services)
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EmailLog, SmsLog, WhatsAppLog
from .serializers import (
    EmailRequestSerializer, EmailResponseSerializer,
    SmsRequestSerializer, SmsResponseSerializer,
    WhatsAppRequestSerializer, WhatsAppResponseSerializer
)


# ============ EMAIL ENDPOINTS ============

@api_view(['POST'])
def send_email(request):
    """
    Send Email - POST /api/email/send
    """
    # Validate request data
    serializer = EmailRequestSerializer(data=request.data)
    
    if serializer.is_valid():
        # Create email log
        email_log = EmailLog.objects.create(
            email_to=serializer.validated_data['emailTo']
        )
        
        # Return response
        response_serializer = EmailResponseSerializer(email_log)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    # Return validation errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_emails(request):
    """
    Get All Emails - GET /api/email/list
    """
    # Get all email logs ordered by timestamp (descending)
    emails = EmailLog.objects.all()
    
    # Serialize the data
    serializer = EmailResponseSerializer(emails, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


# ============ SMS ENDPOINTS ============

@api_view(['POST'])
def send_sms(request):
    """
    Send SMS - POST /api/sms/send
    """
    # Validate request data
    serializer = SmsRequestSerializer(data=request.data)
    
    if serializer.is_valid():
        # Create SMS log
        sms_log = SmsLog.objects.create(
            mobile_number=serializer.validated_data['mobileNumber'],
            message=serializer.validated_data['message']
        )
        
        # Return response
        response_serializer = SmsResponseSerializer(sms_log)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    # Return validation errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_sms(request):
    """
    Get All SMS - GET /api/sms/list
    """
    # Get all SMS logs ordered by timestamp (descending)
    sms_list = SmsLog.objects.all()
    
    # Serialize the data
    serializer = SmsResponseSerializer(sms_list, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


# ============ WHATSAPP ENDPOINTS ============

@api_view(['POST'])
def send_whatsapp(request):
    """
    Send WhatsApp - POST /api/whatsapp/send
    """
    # Validate request data
    serializer = WhatsAppRequestSerializer(data=request.data)
    
    if serializer.is_valid():
        # Create WhatsApp log
        whatsapp_log = WhatsAppLog.objects.create(
            mobile_number=serializer.validated_data['mobileNumber'],
            message=serializer.validated_data['message']
        )
        
        # Return response
        response_serializer = WhatsAppResponseSerializer(whatsapp_log)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    # Return validation errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_whatsapp(request):
    """
    Get All WhatsApp - GET /api/whatsapp/list
    """
    # Get all WhatsApp logs ordered by timestamp (descending)
    whatsapp_list = WhatsAppLog.objects.all()
    
    # Serialize the data
    serializer = WhatsAppResponseSerializer(whatsapp_list, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)