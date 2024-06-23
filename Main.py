import base64
import os
from pathlib import Path
from radio_test.Encoder import Encoder
from cryptography.fernet import Fernet
import socket


HOST, PORT = '127.1.1.19', 5734


class Main:
    # Establish operating path for receiving...
    def __init__(self, op_type):
        self.operating_path = str(Path.home()) + "/radioreceiver/directory/operations/working.rdo"
        self.op_type = None
        self.fernet = Fernet(os.environ['RADIO_KEY'])

    def set_operating_path(self, reg_path):
        self.operating_path = reg_path

    def get_operating_path(self):
        return self.operating_path

    def set_operating_type(self, op_type):
        self.op_type = op_type

    def decode_transmission(self, message):
        return self.fernet.decrypt(base64.b64decode(message)).decode()


# Testing section
# Encode and send
os.environ['RADIO_KEY'] = Fernet.generate_key().decode()
e = Encoder(str(Path.home()) + "/radioreceiver/directory/operations/working.rdo")
operating_string = e.string_b64("ECHO 10-4")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(operating_string)
    data = s.recv(1024)

# DECODE AND RECEIVE
m = Main('string')
print(f"DECODED MESSAGE: {m.decode_transmission(data)!r}")

