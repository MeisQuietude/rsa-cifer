import rsa
from cifer.rsa.abscoder import AbstractCoder
from cifer.rsa.exception import MessageNotFoundException


class Encoder(AbstractCoder):
    def __init__(self):
        super().__init__()

    def encode_message(self, message = None, message_in = None, message_out = 'msg.encoded.txt'):

        if message is None and message_in is None:
            raise MessageNotFoundException

        if message is None:
            with open(message_in, 'r') as f:
                message = f.read()

        with open(self.key_dir / 'key.pub', 'r') as f:
            key = f.read()[10:-1].split(',')

        encoded = rsa.encrypt(message.encode('utf8'), rsa.PublicKey(int(key[0]), int(key[1])))

        with open(message_out, 'wb') as f:
            f.write(encoded)

        print('[+] Message Encoded to', message_out)


if __name__ == '__main__':
    encoder = Encoder()
    encoder.encode_message('Hello world!')