from . import models
from . import serializer

class Mess:
    def __init__(self,request=None,*args,**kwargs) -> None:
        self.request = request
        if not self.request:
            raise AssertionError("request object is not provided")

    def get_mess(self,id=None):
        if not id:
            raise AssertionError("Provide mess id")
        mess = models.Mess.objects.filter(id=id)
        serializer_data = serializer.MessSerializer(data=mess[0])
        data = serializer.MessSerializer(mess[0]).data
        print(data)
        return data
        
    def add_mess(self):
        name = self.request.data.get('name',None)
        price = self.request.data.get('price',None)
        if not name:
            raise AssertionError("Provide mess name")
        if not price:
            raise AssertionError("Provide price of mess")
        
        mess = models.Mess(
            name = name,
            price = price
        )
        mess.save()
        return mess.id