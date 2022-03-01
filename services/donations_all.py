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
        return self.donations_bitcoin.get_value_in_dollars() + \
            self.donations_ethereum.get_value_in_dollars() + \
            self.donations_usdt.get_value_in_dollars() + \
            self.donations_polkadot.get_value_in_dollars()
