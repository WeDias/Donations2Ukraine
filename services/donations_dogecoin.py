import requests
from .donations import Donations


class DonationsDogecoin(Donations):

    BASE_URL = 'https://api.blockchair.com'
    DOGE_ADDRESS = 'DS76K9uJJzQjCFvAbpPGtFerp1qkJoeLwL'

    def get_value_in_dollars(self) -> float:
        response = requests.get(f'https://api.blockchair.com/dogecoin/dashboards/address/DS76K9uJJzQjCFvAbpPGtFerp1qkJoeLwL')
        value_in_dollars = response.json()['data'][self.DOGE_ADDRESS]['address']['received_usd']
        return value_in_dollars
