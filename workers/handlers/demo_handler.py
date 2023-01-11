def handler(connection, method, properties, body):
    print('--- DEMO HANDLER ---')
    print(f'connection: {connection}')
    print(f'method: {method}')
    print(f'properties: {properties}')
    print(f'Received: {body}')
    connection.basic_ack(delivery_tag=method.delivery_tag)
