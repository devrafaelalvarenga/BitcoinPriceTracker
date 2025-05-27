import requests
from datetime import datetime


def extract():
    url = "https://api.coinbase.com/v2/prices/spot"
    version = '1.0'
    try:
        response = requests.get(url)
        raw_data = response.json()
        if 'data' in raw_data and 'amount' in raw_data['data']:
            if 'metadata' not in raw_data:
                raw_data['metadata'] = {}
            raw_data['metadata']['timestamp'] = datetime.now(
            ).isoformat()
            raw_data['metadata']['version'] = version
            return raw_data
        else:
            print("Unexpected response format:", raw_data)
            return None
    except requests.excepitions.ConnectionError as ConnectionError:
        print(f"Connection error:", {ConnectionError})
        return None
    except requests.exceptions.ConnectTimeout as ConnectTimeout:
        print(f"Connection timed out:", {ConnectTimeout})
        return None
    except requests.exceptions.HTTPError as HTTPError:
        print(f"HTTP error:", {HTTPError})
        return None
    except requests.exceptions.RequestException as RequestException:
        print(f"Request exception:", {RequestException})
        return None
