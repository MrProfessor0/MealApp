from rest_framework.response import Response

class StandardResponse(Response):
    def __init__(self, status_code:str=None, message:str=None, data:dict=None, *args, **kwargs) -> None:
        if not status_code:
            raise AssertionError("Status code not provided")
        if not message:
            raise AssertionError("Message is not provided")
        
        response = {}
        response['status_code'] = status_code
        response['message'] = message
        if data:
            response['data'] = data

        super().__init__(status=status_code, data=response, content_type="application/json", *args, **kwargs)
