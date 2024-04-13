from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .classes import Mess
import json

# Create your views here.
class MessView(APIView):
    def get(self,request=None,id=None,format=None):
        try:
            mess = Mess(request)
            response = mess.get_mess(id=id)
            return Response(status=200,data={"message":response},content_type="application/json")
        except AssertionError as e:
            return Response(status=500,data=e.args[0],content_type="application/json")

    def post(self,request=None,format=None):
        try:
            mess = Mess(request)
            response = mess.add_mess()
            return Response(status=200,data={"message":response},content_type="application/json")
        except AssertionError as e:
            return Response(status=500,data=e.args[0],content_type="application/json")
            
