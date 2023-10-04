from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response
from django.views.decorators.csrf import csrf_exempt

class AirtelCallback(APIView):
    def post(self, request):
        message = "Listed products \n 1. Cups\n2.plates"
        return response.Response(message)
