from . import config


class SuperiorRobotBrain:
    def handle_message(self, user, text):
        if config.USERNAME.lower() in text.lower():
            return "~~TUTURUUU~~"
