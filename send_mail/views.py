from django.shortcuts import render
from rest_framework.views import APIView
from .async_send_mail import send_single_mail
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
class SendMail(APIView):
    def post(self,request):
        send_single_mail()
        return Response(status=status.HTTP_202_ACCEPTED)
