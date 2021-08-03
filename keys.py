import binascii
from network import LoRa


def get_app_eui(lora):
    my_mac = binascii.hexlify(lora.mac())
    if my_mac == b'70b3d54999d8d21a':
        app_eui = '70B3D57ED0006DFF'
    else:
        print ("Unknown Device EUI")
        app_eui = 0

    return binascii.unhexlify(app_eui)


def get_app_key(lora):
    my_mac = binascii.hexlify(lora.mac())
    if my_mac == b'70b3d54999d8d21a':
        app_key = '40E36573247B67AB5BD02EA4ECA6C93C'
    else:
        print ("Unknown Device EUI")
        app_key = 0

    return binascii.unhexlify(app_key)
