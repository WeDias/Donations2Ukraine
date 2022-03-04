import requests
from .donations import Donations


class DonationsUSDT(Donations):

    BASE_URL = 'https://api.blockchair.com'
    ETH_ADDRESS = '0x165cd37b4c644c2921454429e7f9358d18a45e14'
    USDT_ADDRESS = '0xdac17f958d2ee523a2206206994597c13d831ec7'

    def get_value_in_dollars(self) -> float:
        response = requests.get(f'{self.BASE_URL}/ethereum/erc-20/{self.USDT_ADDRESS}/'
            f'dashboards/address/{self.ETH_ADDRESS}')
        value_in_dollars = response.json()['data'][self.ETH_ADDRESS]['address']['received_approximate']
        return value_in_dollars
