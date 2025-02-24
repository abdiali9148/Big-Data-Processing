#               Copyright © DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it isn't allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macrame, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).

import unittest

from util import record_matches_fips, record_is_all_industries, record_is_software_industry, get_fips, get_estabs, get_emplvl, get_wages


class TestUtil(unittest.TestCase):
    def setUp(self):
        self.all_ind_10_good = '"02016","0","10","75","0","2022","A","",2,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.all_ind_100_bad = '"29510","0","100","75","0","2022","A","",2,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.software_513210_good = '"02016","5","513210","75","0","2022","A","",2,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.software_51321_bad = '"CS496","5","51321","75","0","2022","A","",2,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.software_5132_bad = '"US000","5","5132","75","0","2022","A","",2,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.fips_bad = '"50000","5","10","72","0","2022","A","",22,605,47017021,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")
        self.industry_bad = '"31079","0","1337","72","0","2022","A","",22,605,47017021,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")
        self.ownership_bad = '"31079","2","10","72","0","2022","A","",22,605,47017021,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")
        self.areas = {
                "02016": "TEST AREA A",
                "31079": "TEST AREA B",
                "29510": "TEST AREA C",
                }

    def test_get_emplvl(self):
        self.assertEqual(1, get_emplvl(self.all_ind_10_good))
        self.assertEqual(605, get_emplvl(self.fips_bad))
        self.assertEqual(605, get_emplvl(self.industry_bad))

    def test_get_estabs(self):
        self.assertEqual(2, get_estabs(self.all_ind_10_good))
        self.assertEqual(22, get_estabs(self.fips_bad))
        self.assertEqual(22, get_estabs(self.industry_bad))

    def test_get_fips(self):
        self.assertEqual("02016", get_fips(self.all_ind_10_good))
        self.assertEqual("50000", get_fips(self.fips_bad))
        self.assertEqual("31079", get_fips(self.industry_bad))

    def test_get_wages(self):
        self.assertEqual(59925, get_wages(self.all_ind_10_good))
        self.assertEqual(47017021, get_wages(self.fips_bad))
        self.assertEqual(47017021, get_wages(self.industry_bad))

    def test_record_matches_fips(self):
        self.assertTrue(record_matches_fips(self.all_ind_10_good, self.areas))
        self.assertTrue(record_matches_fips(self.software_513210_good, self.areas))
        self.assertTrue(record_matches_fips(self.ownership_bad, self.areas))
        self.assertFalse(record_matches_fips(self.software_5132_bad, self.areas))
        self.assertFalse(record_matches_fips(self.software_51321_bad, self.areas))
        self.assertFalse(record_matches_fips(self.fips_bad, self.areas))

    def test_record_is_all_industries(self):
        self.assertTrue(record_is_all_industries(self.all_ind_10_good))
        self.assertFalse(record_is_all_industries(self.all_ind_100_bad))
        self.assertFalse(record_is_all_industries(self.software_513210_good))
        self.assertFalse(record_is_all_industries(self.industry_bad))
        self.assertFalse(record_is_all_industries(self.ownership_bad))

    def test_record_is_software_industry(self):
        self.assertTrue(record_is_software_industry(self.software_513210_good))
        self.assertFalse(record_is_software_industry(self.all_ind_10_good))
        self.assertFalse(record_is_software_industry(self.all_ind_100_bad))
        self.assertFalse(record_is_software_industry(self.software_5132_bad))
        self.assertFalse(record_is_software_industry(self.software_51321_bad))
        self.assertFalse(record_is_software_industry(self.industry_bad))
