from csv import DictReader
import requests
from .donations import Donations


class DonationsPolkadot(Donations):

    BASE_URL = 'https://api.dotscanner.com'
    POLKADOT_ADDRESS = '1x8aa2N2Ar9SQweJv9vsuZn3WYDHu7gMQu1RePjZuBe33Hv'

    def get_value_in_dollars(self) -> float:
        response = requests.get(f'{self.BASE_URL}/stats/prices/dot').json()
        polkadot_price = response['data']['price']

        value_in_dollars = 0
        response = requests.get(f'{self.BASE_URL}/accounts/{self.POLKADOT_ADDRESS}/transfers_csv?chain=Polkadot')
        for transaction in DictReader(response.text.split('\n')):
            if transaction['To'] == self.POLKADOT_ADDRESS:
                value_in_dollars += float(transaction['Amount']) * polkadot_price
        return value_in_dollars
