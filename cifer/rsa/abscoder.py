import os
import re
from pathlib import Path
from abc import ABC, abstractmethod
from cifer.rsa.exception import RSAKeyNotFoundException


class AbstractCoder(ABC):

    @abstractmethod
    def __init__(self, public_key = None, key_directory = Path('.rsa/')):
        self.public = public_key
        self.key_dir = key_directory

        print('[?] Check for valid RSA key...')
        try:
            assert os.path.exists(key_directory / 'key') and os.path.exists(key_directory / 'key.pub')

            if public_key is None:
                with open(key_directory / 'key.pub') as f:
                    key = f.read()
                    assert re.compile("^PublicKey\(\d+, \d+\)").match(key) is not None
                    self.public = key

            print('[+] RSA key is valid.')

        except AssertionError:
            raise RSAKeyNotFoundException()