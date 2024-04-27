from . import models
from . import serializer


class User:
    def __init__(self,request = None) -> None:
        self.request = request
        if not request:
            raise AssertionError("request object is not provided")
        return

    def add_user(self):
        data = self.request.data
        print(data)
        paramters = ['mobile_number', 'email', 'first_name', 'last_name', 'password']
        for params in paramters:
            if params not in data:
                raise AssertionError("{} is not provided.".format(' '.join(params.split("_")).title()))
        
        user = models.User.objects.create_user(
            mobile_number = data.get('mobile_number'),
            password = data.get('password'),
            email = data.get('email'),
            first_name = data.get('first_name'),
            last_name = data.get('last_name')
        )
        serialized_data = serializer.UserSerializer(user)
        serialized_data = serialized_data.data
        return serialized_data

    def list_user(self):
        user_list = models.User.objects.all()
        serializer_data = serializer.UserSerializer(user_list,many=True)
        serializer_data = serializer_data.data
        return serializer_data
    
    def get_user(self,id=None):
        if not id:
            raise AssertionError("User id not provided.")

        user = models.User.objects.filter(id=id)
        serializer_data = serializer.UserSerializer(user[0])
        serializer_data = serializer_data.data
        return serializer_data   

    def update_user(self,id=None):
        if not id:
            raise AssertionError("User Id is not provided")
            
        user = models.User.objects.filter(id=id)
        if not user:
            raise AssertionError("Provide valid user Id")

        data = self.request.data
        # print(dir(user[0]))
        user = user[0]
        for key, value in data.items():
            setattr(user, key, value)
        user.save()

    def delete_user(self,id=None):
        if not id:
            raise AssertionError("User Id is not provided")
            
        user = models.User.objects.filter(id=id)
        if not user:
            raise AssertionError("Provide valid user Id")

        data = self.request.data
        # print(dir(user[0]))
        user = user[0]
        user.is_active = True
        user.is_active = True

        user.save()