import os

from irc.client import SimpleIRCClient


class KakuClient(SimpleIRCClient):
    URL = 'irc.twitch.tv'
    PORT = 6667
    USERNAME = 'MechaKaku'
    PASSWORD = os.getenv('MECHAKAKU_PASSWORD')
    CHANNEL = '#kakusho'

    def __init__(self):
        if not self.PASSWORD:
            raise Exception("MECHAKAKU_PASSWORD environment variable not set.")
        super().__init__()

    def start(self):
        self.connect(self.URL,
                     self.PORT,
                     self.USERNAME,
                     password=self.PASSWORD)
        self.connection.join(self.CHANNEL)
        #super().start()

    def post_message(self, text):
        self.connection.send_raw("PRIVMSG {0} :{1}".format(self.CHANNEL, text))


if __name__ == '__main__':
    print('bot time go!')

    cl = KakuClient()
    cl.start()
    cl.post_message('BOOP BEEP')
