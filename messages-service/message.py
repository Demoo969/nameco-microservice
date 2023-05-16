from nameko.rpc import rpc
import json

class MessagesService:
    name = "messages_service"

    @rpc
    def get_message(self,responce):
        return f"This is a static message. {responce}\n"

    @rpc
    def post_message(self,message,message_id):   
        return json.dumps({'Status: ': f"Message {message} sent with ID {message_id}"})
