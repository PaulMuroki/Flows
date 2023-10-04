from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response
from ussd.core import UssdView, UssdRequest,UssdResponse
from django.http import HttpResponse
import os
import re

class AirtelCallback(APIView):
    def post(self, request):
        message = "Listed products \n 1. Cups\n2.plates"
        return response.Response(message)

class AirtelUSSDFlow(UssdView):
    customer_journey_namespace = "TEST"
    path = os.path.dirname(os.path.abspath(__file__))
    customer_journey_conf = path + "/ussd_file.yml"

    def get(self, request):
        phone_number = request.query_params.get('msisdn', '')
        user_input = request.query_params.get('input', '')
        session_id = request.query_params.get('session_id', '')
        return UssdRequest(
            session_id=str(session_id),
            phone_number=phone_number,
            ussd_input=user_input,
            language='en',
            customer_journey_namespace=self.customer_journey_namespace)

    def ussd_response_handler(self, ussd_response):
        if isinstance(ussd_response, UssdResponse):
            session_status = ussd_response.status
            ussd_text = str(ussd_response)
            ussd_response = HttpResponse(ussd_text)
            ussd_response['Freeflow'] = 'FB'
            if session_status:
                ussd_response['Freeflow'] = 'FC'
        else:
            ussd_response = HttpResponse(status=500)
        return ussd_response
