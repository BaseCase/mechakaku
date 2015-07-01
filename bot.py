from irc.client import SimpleIRCClient

import config


class KakuClient(SimpleIRCClient):
    def __init__(self):
        if not config.PASSWORD:
            raise Exception("MECHAKAKU_PASSWORD environment variable not set.")
        super().__init__()

    def start(self):
        self.connect(config.URL,
                     config.PORT,
                     config.USERNAME,
                     password=config.PASSWORD)
        self.connection.join(config.CHANNEL)
        cl.post_message('/me boots up')
        super().start()

    def post_message(self, text):
        self.connection.send_raw("PRIVMSG {0} :{1}".format(config.CHANNEL, text))

    def on_pubmsg(self, connection, event):
        user = event.source.split('!')[0]
        text = event.arguments[0]

        # figure out what to do based on text (this belongs in a new class probably)
        if config.USERNAME.lower() in text.lower():
            self.post_message("~TUTURUUUU~")

    def on_ctcp(self, connection, event):
        #CTCP is the type of event that happens when someone does a '/me' command
        print("We don't do anything with these right now...")


if __name__ == '__main__':
    print('bot time go!')

    cl = KakuClient()
    cl.start()
