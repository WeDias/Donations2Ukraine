from .donations import Donations


class DonationsPolkadot(Donations):

    BASE_URL = ''
    POLKADOT_ADDRESS = '1x8aa2N2Ar9SQweJv9vsuZn3WYDHu7gMQu1RePjZuBe33Hv'

    def get_value_in_dollars(self) -> float:
        return 0 # TODO: get total value of donations in polkadot
