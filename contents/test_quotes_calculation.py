import pytest
from quotes_calculation import get_quote, get_access_token

class TestQuotes:
    # access token for API
    access_token = get_access_token()
    
    # client object to test
    test_client_youth = {'full_name': 'Dea Test',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-18',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 1,
        'name_1': 'Dea Test',
        'dob_1': '2000-11-29',
        'name_2': '',
        'dob_2': '',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_client_mid = {'full_name': 'Dos Test',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-18',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-02-15',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 1,
        'name_1': 'Dea Test',
        'dob_1': '1980-11-29',
        'name_2': '',
        'dob_2': '',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_client_senior = {'full_name': 'Old Test',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-09',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 1,
        'name_1': 'Dea Test',
        'dob_1': '1950-11-29',
        'name_2': '',
        'dob_2': '',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_client_on = {'full_name': 'Dos Test',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-18',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 1,
        'name_1': 'Dea Test',
        'dob_1': '2000-11-29',
        'name_2': '',
        'dob_2': '',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_client_qc = {'full_name': 'Dos Test',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-18',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Quebec',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 1,
        'name_1': 'Dea Test',
        'dob_1': '2000-11-29',
        'name_2': '',
        'dob_2': '',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_client_ab = {'full_name': 'Dos Test',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-18',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Alberta',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 1,
        'name_1': 'Dea Test',
        'dob_1': '2000-11-29',
        'name_2': '',
        'dob_2': '',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_client_short_trip = {'full_name': 'Short Test',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-09',
        'trip_start': '2026-02-15',
        'dest_arrival': '2026-02-15',
        'end': '2026-03-01',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 1,
        'name_1': 'Dea Test',
        'dob_1': '1980-11-29',
        'name_2': '',
        'dob_2': '',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_client_long_trip = {'full_name': 'Long Test',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-09',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-01',
        'end': '2026-08-01',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 1,
        'name_1': 'Dea Test',
        'dob_1': '1980-11-29',
        'name_2': '',
        'dob_2': '',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_multiclient2 = {'full_name': 'Multi Two',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-09',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 2,
        'name_1': 'Dea Test',
        'dob_1': '1980-11-29',
        'name_2': 'Child Test',
        'dob_2': '2013-10-01',
        'name_3': '',
        'dob_3': '',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_multiclient3 = {'full_name': 'Multi Three',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-09',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 3,
        'name_1': 'Dea Test',
        'dob_1': '1980-11-29',
        'name_2': 'Child Test',
        'dob_2': '2013-10-01',
        'name_3': 'Child Second',
        'dob_3': '2008-09-03',
        'name_4': '',
        'dob_4': '',
        'name_5': '',
        'dob_5': ''
    }

    test_multiclient4 = {'full_name': 'Multi Four',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-09',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 4,
        'name_1': 'Dea Test',
        'dob_1': '1980-11-29',
        'name_2': 'Child Test',
        'dob_2': '2013-10-01',
        'name_3': 'Child Second',
        'dob_3': '2008-09-03',
        'name_4': 'Parent Two',
        'dob_4': '1979-10-01',
        'name_5': '',
        'dob_5': ''
    }

    test_multiclient5 = {'full_name': 'Multi Five',
        'email': 'andrea.britto@gmail.com',
        'submit': '2026-01-09',
        'trip_start': '2026-02-01',
        'dest_arrival': '2026-02-02',
        'end': '2026-03-02',
        'dest_country': 'Canadá',
        'dest_region': 'Ontario',
        'depart_region': '_Fora do Canadá',
        'num_travellers': 5,
        'name_1': 'Dea Test',
        'dob_1': '1980-11-29',
        'name_2': 'Child Test',
        'dob_2': '2013-10-01',
        'name_3': 'Child Second',
        'dob_3': '2008-09-03',
        'name_4': 'Parent Two',
        'dob_4': '1979-10-01',
        'name_5': 'Child Three',
        'dob_5': '2001-11-11'
    }

    # Coverage unit tests

    def test_quotes_10000(self):
        assert_value = get_quote(10000, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 74.52

    def test_quotes_25000(self):
        assert_value = get_quote(25000, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_50000(self):
        assert_value = get_quote(50000, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_100000(self):
        assert_value = get_quote(100000, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100
    
    def test_quotes_20000(self):
        assert_value = get_quote(200000, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_30000(self):
        assert_value = get_quote(300000, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_50000(self):
        assert_value = get_quote(500000, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100 

    # Age Test
        # Trip length fixed 1-Month
        # Coverage 100 000

    recom_coverage = 100000

    def test_quotes_youth(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_youth)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 99.18

    def test_quotes_mid(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_senior(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_senior)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    # Destination Region
        # ON, QC, AB
        # fixed client youth age, 30 Days
    
    def test_quotes_on(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_on)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 99.18

    def test_quotes_qc(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_qc)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_ab(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_ab)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100
    
    # Trip Length
        # Short (2-weeks), Mid (1-Month), Long (6-Months)
        # Fixed mid age

    def test_quotes_short_trip(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_short_trip)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_mid_trip(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_mid)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_long_trip(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_client_long_trip)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    
    # Multi travellers
        # 2, 3, 4, 5 people

    def test_quotes_multi2(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_multiclient2)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_multi3(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_multiclient3)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_multi4(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_multiclient4)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100

    def test_quotes_multi5(self):
        assert_value = get_quote(self.recom_coverage, self.access_token, self.test_multiclient5)['availablePlanPrices'][0]['ratedPrice']['total']
        assert assert_value == 100    

