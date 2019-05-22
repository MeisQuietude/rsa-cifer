
class RSAKeyNotFoundException(Exception):

    def __init__(self):
        super().__init__('RSA Key does not exist yet or not found')
        self.errors = 'RSA Key not found'

class MessageNotFoundException(Exception):

    def __init__(self):
        super().__init__('Message to encode/decode not found (probably incorrect path)')
        self.errors = 'Message not found'