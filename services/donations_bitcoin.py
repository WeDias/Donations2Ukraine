import requests
from .donations import Donations


class DonationsBitcoin(Donations):

    BASE_URL = 'https://api.blockchair.com'
    BTC_ADDRESS = '357a3So9CbsNfBBgFYACGvxxS6tMaDoa1P'

    def get_value_in_dollars(self) -> float:
        response = requests.get(f'{self.BASE_URL}/bitcoin/dashboards/address/{self.BTC_ADDRESS}')
        value_in_dollars = response.json()['data'][self.BTC_ADDRESS]['address']['received_usd']
        return value_in_dollars
