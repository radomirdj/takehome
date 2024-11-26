import dspy
from typing import Optional
from dspy.datasets import DataLoader
import os
from models import ChatHistory
from .responder import ResponderModule
from dspy.teleprompt import KNNFewShot

class ChatterModule(dspy.Module):
    def __init__(self, examples: Optional[dict]):
        super().__init__()
        self.responder = ResponderModule()
        if(examples):
            # Optimise responder
            dl = DataLoader()
            splits = dl.train_test_split(examples, train_size=0.8)
            trainset = splits['train']
            devset = splits['test']
            knn_optimizer = KNNFewShot(k=3, trainset=trainset)
            self.responder = knn_optimizer.compile(
                student=self.responder,
                trainset=trainset,
                valset=devset
            )

    def forward(
        self,
        chat_history: ChatHistory,
    ):
        return self.responder(chat_history=chat_history)