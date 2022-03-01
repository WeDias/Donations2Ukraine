import requests
from .donations import Donations


class DonationsEthereum(Donations):

    BASE_URL = 'https://api.blockchair.com'
    ETH_ADDRESSES = [
        '0x165cd37b4c644c2921454429e7f9358d18a45e14',
        '0x4508401bade71ae75fe70c97fe585d734f975502' # ONG UkraineDAO address
    ]

    def get_value_in_dollars(self) -> float:
        value_in_dollars = 0
        for eth_address in self.ETH_ADDRESSES:
            response = requests.get(f'{self.BASE_URL}/ethereum/dashboards/address/{eth_address}')
            value_in_dollars += response.json()['data'][eth_address]['address']['received_usd']
        return value_in_dollars
