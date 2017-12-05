from network import LoRa
import socket
import binascii
import struct

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('260117F0'))[0]
nwk_swkey = binascii.unhexlify('B23C90C5097CEE8CEC08871DA510B12A')
app_swkey = binascii.unhexlify('5ACC0A3B3723941BE1BDA45C3D0044B6')

dr_min = 0
dr_max = 3

lora.add_channel(0, frequency=91680000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(1, frequency=91700000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(2, frequency=91720000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(3, frequency=91740000, dr_min=dr_min, dr_max=dr_max)

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))
