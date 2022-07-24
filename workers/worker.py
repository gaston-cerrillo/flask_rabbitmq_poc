import pika


class Worker:
    def __init__(self, queue_name, handler):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()

        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_consume(queue=queue_name,
                              on_message_callback=handler)
        channel.basic_qos(prefetch_count=1)
        channel.start_consuming()
