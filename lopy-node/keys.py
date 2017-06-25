import binascii
from network import LoRa


def get_app_eui(lora):
    if binascii.hexlify(lora.mac()) == b'70b3d5499aa88cb0':
        return binascii.unhexlify('70B3D57EF00033F7')
    elif binascii.hexlify(lora.mac()) == b'70b3d5499953cf10':
        return binascii.unhexlify('70B3D57EF00033F7')
    else:
        print ("Unknown Device EUI")
        return 0


def get_app_key(lora):
    if binascii.hexlify(lora.mac()) == b'70b3d5499aa88cb0':
        return binascii.unhexlify('E94327EF2131034018FB987AACF30FF3')
    elif binascii.hexlify(lora.mac()) == b'70b3d5499953cf10':
        return binascii.unhexlify('5D167631DD714E4A040FE27404682C20')
    else:
        print ("Unknown Device EUI")
        return 0
