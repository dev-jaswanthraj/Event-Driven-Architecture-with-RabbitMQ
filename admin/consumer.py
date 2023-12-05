import pika
import json, os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'admin.settings')
django.setup()

from product.models import Product


params = pika.URLParameters('amqps://dkfqeato:AeeLcz702mfz_Ctg_kql6R7vM3wuOl7U@mouse.rmq5.cloudamqp.com/dkfqeato')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    data = json.loads(body)
    product = Product.objects.get(id = data)
    product.likes = product.likes + 1
    product.save()

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
channel.close()