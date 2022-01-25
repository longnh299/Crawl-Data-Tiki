import pika
import time
import pandas as pd
import requests
import json


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='bich da ta', durable=True)
print('Đợi 1 tí nha')


def callback(ch, method, properties, body):
    datarbmq=[]
    datarbmq.append(body)
    print(body)
    df = pd.DataFrame(datarbmq)
    df.to_csv("dataokeoke.csv", mode="a", index=False, header=False)
    datarbmq=[]
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='bich da ta', on_message_callback=callback)
channel.start_consuming()
