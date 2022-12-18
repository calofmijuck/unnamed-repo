import socket
import ssl
import sys

class IRC:

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.irc.settimeout(2)

    def connect(self, server, channel, port, botnick):
        print("Connecting to " + server)
        self.irc.connect((server, port))
        self.irc = ssl.wrap_socket(self.irc)
        self.irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :PikachuBot\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

    def join(self, channel):
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

    def get_text(self):
        try:
            text = self.irc.recv(2048).decode("UTF-8")
            if text.find('PING') != -1:
                self.irc.send(bytes('PONG ' + text.split() [1] + '\r\n', "UTF-8"))
            if text.find('INVITE') != -1:
                self.irc.send(bytes('JOIN ' + text.split() [1] + '\r\n', "UTF-8"))
            return text

        except (ConnectionResetError, socket.timeout) as e: pass

    def send(self, chan, msg):
        cmd = "PRIVMSG " + chan + " :" + msg + "\n"
        self.irc.send(bytes(cmd, "UTF-8"))
        print("SENT: " + cmd, end="")

    def give_op(self, chan, user):
        cmd = "MODE " + chan + " +o " + user + "\n"
        self.irc.send(bytes(cmd, "UTF-8"))
        print("SENT: " + cmd, end="")
