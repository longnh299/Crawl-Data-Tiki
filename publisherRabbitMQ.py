import pika
import sys
import time
import json
data ={
    "name":"long",
    "dob":"29/09/200",
    "provide":"ninh binh"
}
msg=json.dumps(data)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.0.2.1'))
channel = connection.channel()

channel.queue_declare(queue='bich da ta', durable=True)

message = ' '.join(sys.argv[1:]) or msg
while(True):
 time.sleep(2)
 channel.basic_publish(
    exchange='',
    routing_key='bich da ta',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()