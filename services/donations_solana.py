import requests
from bs4 import BeautifulSoup
from .donations import Donations


class DonationsSolana(Donations):

    BASE_URL = 'https://aml.slowmist.com/cases/ukraine_crypto_donations_statistics_2022/'
    SOLANA_ADDRESS = '66pJhhESDjdeBBDdkKmxYYd7q6GUggYPWjxpMKNX39KV'

    def get_value_in_dollars(self) -> float:
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        for table_row in soup.findAll('tr'):
            table_data = table_row.findAll('td')
            if not table_data or table_data[0].text != 'Solana' or \
                table_data[1].text != self.SOLANA_ADDRESS:
                continue
            value_in_dollars = float(table_data[-1].text[2:].replace(',', ''))
            return value_in_dollars
