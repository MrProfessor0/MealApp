from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .classess import User
import json
from MealApp.StandardResponse import StandardResponse


class UserView(APIView):
    """
    Operation for users
    """

    def get(self,request,id=None,format=None):
        try:
            if id:
                user = User(request=request)
                data = user.get_user()
                data = user.get_user(id=id)
                return StandardResponse(status_code=200, message="User fetched succesfully", data=data)
            else:
                user = User(request=request)
                data = user.list_user()
                return StandardResponse(status_code=200, message="User list fetched succesfully", data=data)
        except AssertionError as e:
            print(e.args[0])
            return StandardResponse(status_code=400, message=e.args[0])
        except:
            return StandardResponse(status_code=500, message="Something went wrong while fetching user")

    def post(self,request,format=None):
        try:
            user = User(request=request)
            data = user.add_user()
            return Response(data)
        except AssertionError as e:
            print(e.args[0])
            return StandardResponse(status_code=400, message=e.args[0])
        except:
            return StandardResponse(status_code=500, message="Something went wrong while adding user")

    def put(self,request,id=None,format=None):
        try:
            user = User(request=request)
            user.update_user(id=id)
            return Response("success")
        except AssertionError as e:
            print(e.args[0])
            return StandardResponse(status_code=400, message=e.args[0])
        except:
            return StandardResponse(status_code=500, message="Something went wrong while updating user")

    def delete(self,request,id=None,format=None):
        try:
            user = User(request=request)
            user.delete_user(id=id)
            return Response("success")
        except AssertionError as e:
            print(e.args[0])
            return StandardResponse(status_code=400, message=e.args[0])
        except:
            return StandardResponse(status_code=500, message="Something went wrong while updating user")