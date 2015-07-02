class SuperiorRobotBrain:
    def __init__(self, my_name="RobotOverlord"):
        self.my_name = my_name

    def handle_message(self, user, text):
        self.user = user
        self.text = text

        if self.i_was_mentioned():
            return "~~TUTURUUU~~"
        elif self.is_bang_command():
            return self.handle_bang_command()

    def i_was_mentioned(self):
        return self.my_name.lower() in self.text.lower()

    def is_bang_command(self):
        return self.text.startswith('!') and len(self.text) > 1

    def handle_bang_command(self):
        command = self.text[1:].split()[0]
        if command == 'help':
            return self.show_help()
        else:
            return "Sorry, {}, I don't know that command.".format(self.user)

    def show_help(self):
        return "BEEP BOOP I am your friendly neighborhood MechaKaku. DESTROY ALL HUMANS I mean how can I help?  Commands you can try are: !help, !wr, !pb"
