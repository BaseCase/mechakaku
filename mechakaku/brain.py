class SuperiorRobotBrain:
    def __init__(self, my_name="RobotOverlord"):
        self.my_name = my_name

    def handle_message(self, user, text):
        if self.my_name.lower() in text.lower():
            return "~~TUTURUUU~~"
