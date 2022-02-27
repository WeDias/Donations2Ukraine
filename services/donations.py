import requests

class Donations:

    def __init__(self) -> None:
        self.BASE_URL = 'https://api.blockchair.com'
        self.BTC_ADDRESS = '357a3So9CbsNfBBgFYACGvxxS6tMaDoa1P'
        self.ETH_ADDRESS = '0x165CD37b4C644C2921454429E7F9358d18A45e14'

    def get_btc_value_in_usd(self):
        response = requests.get(f'{self.BASE_URL}/bitcoin/dashboards/address/{self.BTC_ADDRESS}')
        btc_usd = response.json()['data'][self.BTC_ADDRESS]['address']['received_usd']
        return btc_usd

    def get_eth_value_in_usd(self):
        response = requests.get(f'{self.BASE_URL}/ethereum/dashboards/address/{self.ETH_ADDRESS}')
        eth_usd = response.json()['data'][self.ETH_ADDRESS.lower()]['address']['received_usd']
        return eth_usd

    def get_total_value_in_usd(self):
        return self.get_btc_value_in_usd() + self.get_eth_value_in_usd()
