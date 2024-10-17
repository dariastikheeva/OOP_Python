class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.messages.remove(msg)

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, n):
        print(cls.messages[-n:])

    @classmethod
    def total_messages(cls):
        return len(cls.messages)
    
class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False