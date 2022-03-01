import concurrent.futures
from .donations import Donations
from .donations_bitcoin import DonationsBitcoin
from .donations_ethereum import DonationsEthereum
from .donations_usdt import DonationsUSDT
from .donations_polkadot import DonationsPolkadot


class DonationsAll(Donations):

    donations_bitcoin = DonationsBitcoin()
    donations_ethereum = DonationsEthereum()
    donations_usdt = DonationsUSDT()
    donations_polkadot = DonationsPolkadot()

    def get_value_in_dollars(self) -> float:
        value_in_dollars = 0
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.donations_bitcoin.get_value_in_dollars),
                executor.submit(self.donations_ethereum.get_value_in_dollars),
                executor.submit(self.donations_usdt.get_value_in_dollars),
                executor.submit(self.donations_polkadot.get_value_in_dollars)
            ]
            for future in concurrent.futures.as_completed(futures):
                value_in_dollars += future.result()
        return value_in_dollars
