from ..extract.extract import extract
from datetime import datetime


def transform(raw_data):
    amount = raw_data['data']['amount']
    base = raw_data['data']['base']
    currency = raw_data['data']['currency']
    timestamp = raw_data['metadata']['timestamp']
    version = raw_data['metadata']['version']
    updated_data = {'amont': amount, 'base': base,
                    'currency': currency, 'timestamp': timestamp, 'version': version}
    return updated_data
