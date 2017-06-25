from network import LoRa
import socket
import binascii
import struct

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, public=True, adr=False, tx_retries=0)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('26011087'))[0]
nwk_swkey = binascii.unhexlify('831D5CCFB0239AB9FDD0A157B9846D90')
app_swkey = binascii.unhexlify('B8D0CC2B00F1D547C6B5BE27F9CFD72D')

dr_min=0
dr_max=3
lora.add_channel(0, frequency=916800000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(1, frequency=917000000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(2, frequency=917200000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(3, frequency=917400000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(4, frequency=917600000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(5, frequency=917800000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(6, frequency=918000000, dr_min=dr_min, dr_max=dr_max)
lora.add_channel(7, frequency=918100000, dr_min=dr_min, dr_max=dr_max)
# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)
s.setblocking(True)
s.send(bytes([0x01, 0x02, 0x04]))
