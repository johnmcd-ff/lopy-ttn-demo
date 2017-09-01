import binascii
from network import LoRa


def get_app_eui(lora):
    my_mac = binascii.hexlify(lora.mac())
    if my_mac == b'70b3d5499fb4e9e7':
        app_eui = '70B3D57ED0006DFF'
    else:
        print ("Unknown Device EUI")
        app_eui = 0

    return binascii.unhexlify(app_eui)


def get_app_key(lora):
    my_mac = binascii.hexlify(lora.mac())
    if my_mac == b'70b3d5499fb4e9e7':
        app_key = 'EEBB85F338C0858F93AEEF3FCDF7BE85'
    else:
        print ("Unknown Device EUI")
        app_key = 0

    return binascii.unhexlify(app_key)
