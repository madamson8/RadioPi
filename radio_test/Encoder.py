import os
from pathlib import Path
import base64
import json
from cryptography.fernet import Fernet


class Encoder:
    def __init__(self, reg_path):
        self.operating_path = reg_path
        self.key = os.environ['RADIO_KEY'].encode()

    def string_b64(self, value):
        fernet = Fernet(self.key)
        enc_message = fernet.encrypt(value.encode())
        encoded_value = base64.b64encode(enc_message)
        return encoded_value
