import paho.mqtt.client as mqtt
from datetime import datetime




def on_internal_message(client, userdata, message):
    global f

    print ('internal message ', message.topic)
    f.write('internal:'+ message.topic+ ' '+  datetime.now().strftime('%Y%m%d%H%M'))


def on_external_message(client, userdata, message):
    global f
    print('external message ', message.topic)
    f.write('external:' + message.topic + ' ' +  datetime.now().strftime('%Y%m%d%H%M'))


def Monitor (connection_mode):
    global f
    # Getting the current date and time

    date = datetime.now().strftime('%Y%m%d%H%M')
    myFileName = f'log{date}.txt'
    f = open(myFileName, 'w')

    global external_client
    global internal_client

    print ('Connection mode: ', connection_mode)


    # The internal broker is always (global or local mode) at localhost:1884
    internal_broker_address = "localhost"
    internal_broker_port = 1884

    if connection_mode == 'global':
        # in global mode, the external broker must be running in internet
        # and must operate with websockets
        # there are several options:
        # a public broker
        external_broker_address = "broker.hivemq.com"
        # our broker (that requires credentials)
        #external_broker_address = "classpip.upc.edu"
        # a mosquitto broker running at localhost (only in simulation mode)
        #external_broker_address = "localhost"

    else:
        # in local mode, the external broker will run always in localhost
        # (either in production or simulation mode)
        external_broker_address = "localhost"

    # the external broker must run always in port 8000
    external_broker_port = 8000


    external_client = mqtt.Client("Motinor external", transport="websockets")
    external_client.on_message = on_external_message
    external_client.connect(external_broker_address, external_broker_port)


    internal_client = mqtt.Client("Monitor_internal")
    internal_client.on_message = on_internal_message
    internal_client.connect(internal_broker_address, internal_broker_port)

    print("Waiting ....")
    external_client.subscribe("autopilotService/#")
    internal_client.subscribe("#")
    internal_client.loop_start()
    external_client.loop_forever()


if __name__ == '__main__':
    import sys
    connection_mode = sys.argv[1] # global or local
    Monitor(connection_mode)
