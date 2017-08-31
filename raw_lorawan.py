from network import LoRa
import socket
import binascii

lora = LoRa(mode=LoRa.LORA, frequency=923400000, device_class=LoRa.CLASS_C)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

d = binascii.hexlify('4087100126200100013d107777819cc695')

s.send(d)
