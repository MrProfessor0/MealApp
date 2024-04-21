from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .classess import User
import json


class UserView(APIView):
    """
    Operation for users
    """

    def get(self,request,id=None,format=None):
        try:
            if id:
                user = User(request=request)
                data = user.get_user(id=id)
                return Response(data)
            else:
                user = User(request=request)
                data = user.list_user()
                return Response(data)
        except AssertionError as e:
            print(e.args[0])
            return Response(e.args[0])    

    def post(self,request,format=None):
        try:
            user = User(request=request)
            data = user.add_user()
            return Response(data)
        except AssertionError as e:
            print(e.args[0])
            return Response(e.args[0])

    