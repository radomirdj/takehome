from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    from_creator: bool
    content: str
    message_time: Optional[datetime]

    def __str__(self):
        role = "YOU" if self.from_creator else "THE FAN"
        basic_details = role
        if(self.message_time is not None):
            basic_details =  self.message_time.strftime('%H:%M %m/%d/%Y') + ' ' + basic_details
        message = basic_details + ": " + self.content
        return message

class ChatHistory(BaseModel):
    messages: List[ChatMessage] = []

    def __str__(self):
        messages = []
        for i, message in enumerate(self.messages):
            message_str = str(message)
            # if i == len(self.messages) - 1 and not message.from_creator:
            #     message_str = (
            #         "(The fan just sent the following message which your message must respond to): "
            #         + message_str
            #     )
            messages.append(message_str)
        return "\n".join(messages)
    
    def model_dump_json(self, **kwargs):
        return str(self)