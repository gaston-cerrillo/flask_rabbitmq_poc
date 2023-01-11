from datetime import datetime
from services.file_service import save_file
from services.db import query
from services.mail import send_mail
from decouple import config
import json


OUTPUT_DOCKER_DIR = config('docker_dir')
REQUIRED_FIELDS = ['query', 'mail']
URL_TO_FILE = config('url_file_reportes')


def handler(connection, method, properties, body):
    print('body: \n', body)
    data = json.loads(body)
    print(f'Received data: {data}')

    filename = f'reporte-{datetime.timestamp(datetime.now())}'
    received_fields = list(set(data.keys()))

    if not all(i in received_fields for i in REQUIRED_FIELDS):
        raise Exception('Some required fields are missing')

    print(f'Generating report {filename}.xlsx\n')
    save_file(query(data["query"]), f'{OUTPUT_DOCKER_DIR}/{filename}.xlsx')

    print('Sending mail\n')
    url_template = f'<a>{URL_TO_FILE}/{filename}</a>'
    send_mail(data['mail'], None, url_template)

    if connection:
        connection.basic_ack(delivery_tag=method.delivery_tag)
