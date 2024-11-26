import dspy

from models import ChatHistory

class Responder(dspy.Signature):
    """
    You are an OnlyFans creator chatting on OnlyFans with a fan.
    You are deciding on what your message should be.
    However, don't mention social media platforms (except OnlyFans) and interactions suggesting in-person meetings with fans.
    """

    chat_history: ChatHistory = dspy.InputField(desc="the chat history")
    current_time: str = dspy.InputField(desc="Contains the current time of fan")

    output: str = dspy.OutputField(
        prefix="Your Message:",
        desc="the exact text of the message you will send to the fan.",
    )