import logging
from flask import Flask, request, Response
from src.business import transfers
from src.utils import environment

environment.set_env()

app = Flask(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


@app.route('/', methods=['POST'])
def listener():
    if request.method == 'POST':

        response = request.json
        subscription = response['event']['subscription']
        event_type = response['event']['log']['type']
        logging.info(f'Receiving {subscription} with type {event_type}')
        if subscription == 'invoice' and event_type == 'credited':
            logging.info("Invoice credited! Transferring to Stark Bank...")
            received_amount = response['event']['log']['invoice'][
                'amount'] - response['event']['log']['invoice']['fee']
            transfers.create(received_amount)
        else:
            logging.info(f'Invoice without status credited - status: '
                         f'{event_type}')

        return Response(status=200)


app.run()
