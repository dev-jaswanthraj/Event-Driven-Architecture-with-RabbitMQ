import pika, json
from main import Product, db, app

params = pika.URLParameters('amqps://dkfqeato:AeeLcz702mfz_Ctg_kql6R7vM3wuOl7U@mouse.rmq5.cloudamqp.com/dkfqeato')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')
with app.app_context():
    def callback(ch, method, properties, body):
        data = json.loads(body)
        print(data)
        if properties.content_type == 'product_created':
            product = Product(
                id = data['id'],
                title = data['title'],
                image = data['image']
            )
            db.session.add(product)
            db.session.commit()
        elif properties.content_type == 'product_updated':
            product = db.session.get(Product, data['id'])
            product.title = data['title']
            product.image = data['image']
            db.session.commit()
        elif properties.content_type == 'product_deleted':
            product = db.session.get(Product, data)
            db.session.delete(product)
            db.session.commit()

    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
    channel.close()