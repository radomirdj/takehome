import os
import json
from models import ChatHistory, ChatMessage
import dspy

def load_examples():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'training_data', 'conversations.json')
    examples = []    
    with open(file_path, 'r') as file:
        data_history = json.load(file)
        for chat_example in data_history:
            # create chat_history for the example
            chat_history = ChatHistory()
            for chat_history_message in chat_example['chat_history']['messages']:
                    chat_history.messages.append(
                        ChatMessage(
                            from_creator=chat_history_message['from_creator'],
                            content=chat_history_message['content'],
                        ),
                    )
            output = chat_example['output']
            example = dspy.Example(chat_history=chat_history, output=output).with_inputs("chat_history")
            examples.append(example)
    return examples
