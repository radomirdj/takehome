import dspy

from models import ChatHistory

class MessageFilterer(dspy.Signature):
    """
    You are admin in the team of OnlyFans creator. You need to make sure that messages from models don't break company rules.
    Message is valid if it doesn't break any rule.
    The rules are:
    * They must not mention social media platforms (except OnlyFans)
    * They should never suggest in-person meetings with fans.
    You will receive the message and return message with filtered out this part.
    """
# Maybe it could happend if whole message is filtered out that we send empty message - to be improved
    creator_message: str = dspy.InputField(desc="Message that OnlyFans creator has written ant that needs tobe validated")

    output: str = dspy.OutputField(
        desc="creators message with filtered out problematic parts.",
    )