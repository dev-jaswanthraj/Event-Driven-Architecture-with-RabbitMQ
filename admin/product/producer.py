#amqps://dkfqeato:AeeLcz702mfz_Ctg_kql6R7vM3wuOl7U@mouse.rmq5.cloudamqp.com/dkfqeato
import pika
import json

params = pika.URLParameters('amqps://dkfqeato:AeeLcz702mfz_Ctg_kql6R7vM3wuOl7U@mouse.rmq5.cloudamqp.com/dkfqeato')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body = json.dumps(body), properties=properties)