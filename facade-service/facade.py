from nameko.web.handlers import http
from nameko.rpc import RpcProxy
import uuid
from bson import ObjectId
import json


class FacadeService:
    name = "facade_service"
    url='http://127.0.0.1:8001/logger'
    logging_rcp = RpcProxy("logging_service")
    messages_rcp = RpcProxy("messages_service")

    @http("POST", "/messages")
    def create_message(self, request):
        message = json.loads(request.get_data(as_text=True))
        message_id = str(uuid.uuid4().hex) #UUID gneration
        self.logging_rcp.log_message(message,message_id)
        
        return self.messages_rcp.post_message(message,message_id) 

    @http("GET", "/messages")
    def get_messages(self, request):
        messages = self.logging_rcp.get_messages()
        responce = ''.join(messages)
        return self.messages_rcp.get_message(responce)  
        







