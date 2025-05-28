from tinydb import TinyDB
from ..extract import extract
from ..transform import transform


def load(updated_data):
    btc_coinbase_api = TinyDB(
        'bitcoinpricetracker/utils/btc_coinbase_api.json')
    btc_coinbase_api.insert(updated_data)
    btc_coinbase_api.close()
