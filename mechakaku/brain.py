from datetime import datetime, timedelta


class SuperiorRobotBrain:
    def __init__(self, my_name="RobotOverlord"):
        self.my_name = my_name

        # some vars to keep track of :j posts (so I don't spam)
        now = datetime.now()
        self.last_posted_colon_jay = now - timedelta(days=1)
        self.last_seen_colon_jay = now - timedelta(days=1)


    def handle_message(self, user, text):
        self.user = user
        self.text = text

        if self.i_was_mentioned():
            return "~~TUTURUUU~~"
        elif self.is_bang_command():
            return self.handle_bang_command()
        elif self.is_colon_jay():
            return self.get_on_the_colon_jay_train()


    def handle_bang_command(self):
        command = self.text[1:].split()[0]
        if command == 'help':
            return self.show_help()
        else:
            return "Sorry, {}, I don't know that command.".format(self.user)


    ###
    # Tests for what type of message we received
    ###

    def is_bang_command(self):
        return self.text.startswith('!') and len(self.text) > 1


    def i_was_mentioned(self):
        return self.my_name.lower() in self.text.lower()


    def is_colon_jay(self):
        return self.text == ":j"


    ###
    # Responses I can give
    ###

    def show_help(self):
        return "BEEP BOOP I am your friendly neighborhood MechaKaku. DESTROY ALL HUMANS I mean how can I help?  Commands you can try are: !help, !wr, !pb"


    def get_on_the_colon_jay_train(self):
        # The idea here is, I don't want to *always* respond to :j, only at a reasonable rate.
        now = datetime.now()
        if (now - self.last_seen_colon_jay < timedelta(minutes=1) and
                now - self.last_posted_colon_jay > timedelta(minutes=1)):
            self.last_posted_colon_jay = now
            self.last_seen_colon_jay = now
            return ":j"
        else:
            self.last_seen_colon_jay = now
