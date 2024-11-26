import dspy

from signatures.message_filterer import MessageFilterer

class FiltererModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.TypedChainOfThought(MessageFilterer)
    
    def forward(
        self,
        creator_message: str,
    ):
        return self.prog(
            creator_message=creator_message,
        )