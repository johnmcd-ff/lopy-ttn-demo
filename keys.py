import binascii
from network import LoRa

def get_app_eui(lora):
    my_mac = binascii.hexlify(lora.mac())
    if my_mac == b'70b3d5499aa88cb0':
        app_eui = '70B3D57EF00033F7'
    elif my_mac == b'70b3d5499953cf10':
        app_eui = '70B3D57EF00033F7'
    elif my_mac == b'70b3d54998252a8b':
        app_eui = '70B3D57ED0006DFF'
    else:
        print ("Unknown Device EUI")
        app_eui = 0

    return binascii.unhexlify(app_eui)


def get_app_key(lora):
    my_mac = binascii.hexlify(lora.mac())
    if my_mac == b'70b3d5499aa88cb0':
        app_key = 'E94327EF2131034018FB987AACF30FF3'
    elif my_mac == b'70b3d5499953cf10':
        app_key = '5D167631DD714E4A040FE27404682C20'
    elif my_mac == b'70b3d54998252a8b':
        app_key = 'F808E877C3B5589D6813BB9645E64136'
    else:
        print ("Unknown Device EUI")
        app_key = 0

    return binascii.unhexlify(app_key)
