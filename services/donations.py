import requests
from cachetools import TTLCache

class Donations:

    BASE_URL = 'https://api.blockchair.com'
    BTC_ADDRESS = '357a3So9CbsNfBBgFYACGvxxS6tMaDoa1P'
    ETH_ADDRESS = '0x165cd37b4c644c2921454429e7f9358d18a45e14'
    USDT_ADDRESS = '0xdac17f958d2ee523a2206206994597c13d831ec7'

    def __init__(self) -> None:
        self.cache = TTLCache(maxsize=1, ttl=60)

    def get_btc_value_in_usd(self) -> float:
        response = requests.get(f'{self.BASE_URL}/bitcoin/dashboards/address/{self.BTC_ADDRESS}')
        btc_in_usd = response.json()['data'][self.BTC_ADDRESS]['address']['received_usd']
        return btc_in_usd

    def get_eth_value_in_usd(self) -> float:
        response = requests.get(f'{self.BASE_URL}/ethereum/dashboards/address/{self.ETH_ADDRESS}')
        eth_in_usd = response.json()['data'][self.ETH_ADDRESS]['address']['received_usd']
        return eth_in_usd

    def get_value_in_usdt(self) -> float:
        response = requests.get(f'{self.BASE_URL}/ethereum/erc-20/{self.USDT_ADDRESS}/dashboards/address/{self.ETH_ADDRESS}')
        usdt = response.json()['data'][self.ETH_ADDRESS]['address']['received_approximate']
        return usdt

    def get_total_value_in_usd(self) -> float:
        if 'donated' not in self.cache:
            self.cache['donated'] = self.get_btc_value_in_usd() + self.get_eth_value_in_usd() + self.get_value_in_usdt()
        return self.cache['donated']
