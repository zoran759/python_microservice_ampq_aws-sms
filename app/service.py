import pika
import sys
import boto3
import os
import json
from dotenv import load_dotenv
from aws.sms import send_sms, data_validate


load_dotenv()
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq_api'))
channel = connection.channel()

exchangeName = 'api_services';
channel.exchange_declare(exchange=exchangeName, exchange_type='topic', durable=True)
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
binding_key = 'service.sms.*'

channel.queue_bind(exchange=exchangeName, queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    #print(" [x] %r:%r" % (method.routing_key, body))
    data=json.loads(body)
    if data_validate(data["data"]):
        send_sms(data["data"])
        print("SMS was successfully sent!")
    else:
        print("SMS phone number or message were not provided!")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
