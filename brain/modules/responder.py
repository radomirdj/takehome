import dspy

from signatures.responder import Responder
from models import ChatHistory
from datetime import datetime

class ResponderModule(dspy.Module):
    def __init__(self):
        super().__init__()
        reasoning = dspy.OutputField(
            prefix="Reasoning: Let's think step by step to decide on our message. We",
        )
        self.prog = dspy.TypedChainOfThought(Responder, reasoning=reasoning)
    
    def forward(
        self,
        chat_history: dict,
    ):
        current_time = datetime.now()
        # current_time should be calculated in fan's timezone
        return self.prog(
            current_time=current_time.strftime('%H:%M %m/%d/%Y'),
            chat_history=ChatHistory.parse_obj(chat_history),
        )