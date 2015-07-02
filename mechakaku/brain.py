from datetime import datetime, timedelta


class SuperiorRobotBrain:
    def __init__(self, my_name="RobotOverlord"):
        self.my_name = my_name

        # some vars to keep track of when I post certain things so I don't spam
        yesterday = datetime.now() - timedelta(days=1)
        self.rate_limited_times = {
            'colon_jay': {
                'last_seen': yesterday,
                'last_posted': yesterday
            },
            'copypasta': {
                'last_seen': yesterday,
                'last_posted': yesterday
            }
        }


    def handle_message(self, user, text):
        self.user = user
        self.text = text

        if self.i_was_mentioned():
            return "~~TUTURUUU~~"
        elif self.is_bang_command():
            return self.handle_bang_command()
        elif self.is_colon_jay():
            return self.get_on_the_colon_jay_train()
        elif self.is_copypasta():
            return self.get_on_the_copypasta_train()


    def handle_bang_command(self):
        command = self.text[1:].split()[0]
        if command == 'help':
            return self.show_help()
        elif command == 'motivate':
            return self.show_motivational_message()
        else:
            return "Sorry, {}, I don't know that command.".format(self.user)


    def rate_limited_message(self, post_type, message):
        # When people in the channel start posting the same thing, join in, but at most once per minute.
        time_tracker = self.rate_limited_times[post_type]
        now = datetime.now()

        if (now - time_tracker['last_seen'] < timedelta(minutes=1) and
                now - time_tracker['last_posted'] > timedelta(minutes=1)):
            time_tracker['last_posted'] = now
            time_tracker['last_seen'] = now
            return message
        else:
            time_tracker['last_seen'] = now


    ###
    # Tests for what type of message we received
    ###

    def is_bang_command(self):
        return self.text.startswith('!') and len(self.text) > 1


    def i_was_mentioned(self):
        return self.my_name.lower() in self.text.lower()


    def is_colon_jay(self):
        return self.text == ":j"

    def is_copypasta(self):
        return len(self.text) > 150


    ###
    # Responses I can give
    ###

    def show_help(self):
        return "BEEP BOOP I am your friendly neighborhood MechaKaku. DESTROY ALL HUMANS I mean how can I help?  Commands you can try are: !help, !motivate"


    def get_on_the_colon_jay_train(self):
        return self.rate_limited_message('colon_jay', ":j")


    def get_on_the_copypasta_train(self):
        return self.rate_limited_message('copypasta', self.text)


    def show_motivational_message(self):
        return "NeverGiveUp NeverGiveUp NeverGiveUp http://www.youtube.com/watch?v=tYzMYcUty6s NeverGiveUp NeverGiveUp NeverGiveUp"
