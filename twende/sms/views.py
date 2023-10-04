from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response
from ussd.core import UssdView
from django.http import HttpResponse

class AirtelCallback(APIView):
    def post(self, request):
        message = "Listed products \n 1. Cups\n2.plates"
        return response.Response(message)

class AirtelUSSDFlow(UssdView):
    customer_journey_namespace = None
    path = os.path.dirname(os.path.abspath(__file__))
    customer_journey_conf = path + "/ussd_file.yml"

    def get(self, requests):
        phone_number = request.query_params.get('MSISDN', '')
        user_input = request.query_params.get('input', '')
        session_id = request.query_params.get('session_id', '')
        return UssdRequest(
            session_id=str(session_id),
            phone_number=re.sub(
                r'\s+',
                '',
                phone_number),
            ussd_input=user_input,
            language=request.META.get(
                "HTTP_USER_LANGUAGE",
                'en'),
            partner_guid=self.partner_guid,
            customer_journey_namespace=self.customer_journey_namespace)

    def ussd_response_handler(self, ussd_response):
        if isinstance(mno_response, UssdResponse):
            ussd_text = str(mno_response)
            ussd_response = HttpResponse(ussd_text)
            ussd_response['Freeflow'] = 'FB'
            if mno_response.status:
                response_['Freeflow'] = 'FC'
        else:
            ussd_response = HttpResponse(status=500)
        return ussd_response
