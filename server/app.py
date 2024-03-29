from flask import Flask, request
from decouple import config
import pika

app = Flask(__name__)

user = config('rabbitmq_user')
password = config('rabbitmq_pass')


@app.route('/')
def index():
    return 'Queue server started successfully'


@app.route('/publish/<queue_name>', methods=['POST'])
def add(queue_name):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq',
                                  credentials=pika.PlainCredentials(
                                      user, password),
                                  heartbeat=600))
    channel = connection.channel()

    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=request.data,
        properties=pika.BasicProperties(
            delivery_mode=2,
        ))
    connection.close()
    return f'Published message to {queue_name}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
