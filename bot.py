from irc.client import SimpleIRCClient

from mechakaku import MechaKaku
import config


class KakuClient(SimpleIRCClient):
    def __init__(self):
        if not config.PASSWORD:
            raise Exception("MECHAKAKU_PASSWORD environment variable not set.")
        self.brain = MechaKaku()
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
        response = self.brain.handle_message(user, text)
        if response:
            self.post_message(response)

    def on_ctcp(self, connection, event):
        #CTCP is the type of event that happens when someone does a '/me' command
        print("We don't do anything with these right now...")


if __name__ == '__main__':
    print('bot time go!')

    cl = KakuClient()
    cl.start()
