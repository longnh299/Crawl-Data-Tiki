import pika
import time
import pandas as pd


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='bich da ta', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

data=[]
def callback(ch, method, properties, body):
    #time.sleep(10)
    data.append(body.decode())
    print(data)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='bich da ta', on_message_callback=callback)
channel.start_consuming()
df=pd.DataFrame(data)
#print(data)
df.to_csv("datarbmq.csv",mode="a",index=False,header=False)

