import config


class MechaKaku:
    def handle_message(self, user, text):
        if config.USERNAME.lower() in text.lower():
            return "~~TUTURUUU~~"
