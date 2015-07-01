from irc.client import Reactor


if __name__ == '__main__':
    print('bot time go!')

    cl = Reactor()
    server = cl.server()
    server.connect('irc.twitch.tv', 6667, 'MechaKaku', password='do not commit the secret!')
    server.join('#kakusho')
    server.send_raw('PRIVMSG #kakusho :BOOP BEEP')
