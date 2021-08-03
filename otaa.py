from network import LoRa
import socket
import binascii
import struct
import keys

def configure_channels():
    # remove all the non-default channels
    if lora.frequency() == 868000000:
        min_channel=3
        max_channel=15
    else:
        min_channel=1
        max_channel=72


    for i in range(min_channel, max_channel):
        lora.remove_channel(i)

    if lora.frequency() == 868000000:
        print("Connecting KotahiNet frequency plan")
        dr_min=0
        dr_max=5
        # New KotahiNet band plan
        lora.add_channel(0, frequency=864862500, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(1, frequency=865062500, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(2, frequency=865402500, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(3, frequency=865602500, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(4, frequency=865985000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(5, frequency=866200000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(6, frequency=866400000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(7, frequency=866600000, dr_min=dr_min, dr_max=dr_max)

    else:
        print("Connecting to AU_915_928 FSB3")

        # Uplink
        dr_min=0
        dr_max=3
        lora.add_channel(0, frequency=916800000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(1, frequency=917000000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(2, frequency=917200000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(3, frequency=917400000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(4, frequency=917600000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(5, frequency=917800000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(6, frequency=918000000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(7, frequency=918200000, dr_min=dr_min, dr_max=dr_max)

        lora.add_channel(8, frequency=918400000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(9, frequency=918600000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(10, frequency=918800000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(11, frequency=919000000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(12, frequency=919200000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(13, frequency=919400000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(14, frequency=919600000, dr_min=dr_min, dr_max=dr_max)
        lora.add_channel(15, frequency=919800000, dr_min=dr_min, dr_max=dr_max)

        # lora.add_channel(0, frequency=918400000, dr_min=dr_min, dr_max=dr_max)
        # lora.add_channel(1, frequency=918600000, dr_min=dr_min, dr_max=dr_max)
        # lora.add_channel(2, frequency=918800000, dr_min=dr_min, dr_max=dr_max)
        # lora.add_channel(3, frequency=919000000, dr_min=dr_min, dr_max=dr_max)
        # lora.add_channel(4, frequency=919200000, dr_min=dr_min, dr_max=dr_max)
        # lora.add_channel(5, frequency=919400000, dr_min=dr_min, dr_max=dr_max)
        # lora.add_channel(6, frequency=919600000, dr_min=dr_min, dr_max=dr_max)
        # lora.add_channel(7, frequency=919800000, dr_min=dr_min, dr_max=dr_max)

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an OTAA authentication parameters
app_eui = keys.get_app_eui(lora)
app_key = keys.get_app_key(lora)

configure_channels()

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    print('Waiting to join...')
    pycom.rgbled(red)
    time.sleep(0.1)
    pycom.rgbled(off)
    time.sleep(2)

pycom.heartbeat(True)

configure_channels()

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
#s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send something to say 'hello'
print('Send 0x01 0x02 0x03')
s.send(bytes([0x01, 0x02, 0x03]))

#set up BUTTON as an input
button = Pin("G17",  mode=Pin.IN,  pull=Pin.PULL_UP)

i = 0
s.setblocking(False)
pycom.heartbeat(False)

from struct import *

baro_id=0x73
temp_id=0x67
hum_id=0x68

baro=1008.0
temp_indoor=20.5
temp_outdoor=14.2
humidity_indoor=65
humidity_outdoor=87

while(1):
    #send using Cayenne Low Power Protocol(LPP) NB: big endian format
    packet = pack('>BBhBBhBBhBBBBBB',1,baro_id,int(baro*10),2,temp_id,int(temp_indoor*10),3,temp_id,int(temp_outdoor*10),4,hum_id,int(humidity_indoor*2),5,hum_id,int(humidity_outdoor*2))
    print("TX:", binascii.hexlify(packet))
    s.send(packet)
    baro+=1
    temp_indoor+=0.1
    temp_outdoor-=0.1
    #print("TX:", i.to_bytes(8))
    #s.send(i.to_bytes(8))
    print("RX:", binascii.hexlify(s.recv(64)))
    pycom.rgbled(green)
    time.sleep(0.1)
    pycom.rgbled(off)
    time.sleep(1)
    if(button() == 0):
        s.send('hi')
        pycom.rgbled(red)
    time.sleep(8.9)
    i+=1
