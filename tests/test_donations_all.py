from services.donations_all import DonationsAll


class TestDonationsAll:

    def test_get_value_in_dollars(self):
        donations_all = DonationsAll()
        assert donations_all.get_value_in_dollars() >= 0
