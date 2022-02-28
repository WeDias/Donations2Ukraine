from services.donations import Donations


class TestDonations:

    def test_get_total_value_in_usd(self):
        donations = Donations()
        assert donations.get_total_value_in_usd() >= 0
