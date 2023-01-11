import pika
from decouple import config


class Worker:
    user = config('rabbitmq_user')
    password = config('rabbitmq_pass')

    def __init__(self, queue_name, handler):
        print('Starting connection ...\n')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='rabbitmq',
                credentials=pika.PlainCredentials(
                    self.user, self.password))
        )
        channel = connection.channel()

        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_consume(queue=queue_name,
                              on_message_callback=handler)
        channel.basic_qos(prefetch_count=1)
        channel.start_consuming()
