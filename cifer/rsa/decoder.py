import rsa

from cifer.rsa.abscoder import AbstractCoder
from cifer.rsa.exception import MessageNotFoundException


class Decoder(AbstractCoder):
    def __init__(self):
        super().__init__()

    def decode_message(self, message=None, message_in='msg.encoded.txt', message_out='msg.decoded.txt'):
        with open(self.key_dir / 'key', 'r') as f:
            key = f.read()[11:-1].split(',')

        msg = message

        try:
            if msg is None:
                with open(message_in, 'rb') as f:
                    msg = f.read()

        except FileNotFoundError:
            raise MessageNotFoundException()

        crypto = rsa.decrypt(msg, rsa.PrivateKey(int(key[0]), int(key[1]), int(key[2]), int(key[3]), int(key[4])))

        with open(message_out, 'w') as f:
            f.write(crypto.decode('utf8'))

        print('[+] Message decoded to', message_in)
        print('[Decoded Text]', crypto.decode('utf8'))


if __name__ == '__main__':
    decoder = Decoder()
    decoder.decode_message()