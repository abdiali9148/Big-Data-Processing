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

from industry_data import IndustryData


class TestIndustryData(unittest.TestCase):
    def setUp(self):
        self.areas = {
                "02016": "TEST AREA A",
                "31079": "TEST AREA B",
                "EMPL0": "Employment Level Area 0",
                "EMPL1": "Employment Level Area 1",
                "ESTB0": "Number Of Establishments Area 0",
                "ESTB1": "Number Of Establishments Area 1",
                "WAGE0": "Wages Area 0",
                "WAGE1": "Wages Area 1",
                }
        #                      fips  own  ind     3   4   year   6   7 8 9
        self.record0 =       '"02016","2","611","75","0","2022","A","",2,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.record1 =       '"31079","1","102","72","0","2022","A","",22,605,47017021,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")
        self.tied_emplvl0 =  '"EMPL0","2","611","75","0","2022","A","",2,777,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.tied_emplvl1 =  '"EMPL1","1","102","72","0","2022","A","",22,777,47017021,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")
        self.tied_estabs0 =  '"ESTB0","2","611","75","0","2022","A","",777,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.tied_estabs1 =  '"ESTB1","1","102","72","0","2022","A","",777,605,47017021,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")
        self.tied_wages0 =   '"WAGE0","2","611","75","0","2022","A","",2,1,777,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        self.tied_wages1 =   '"WAGE1","1","102","72","0","2022","A","",22,605,777,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")

    def test_default_values(self):
        """
        Ensure the attributes of the Report object are named correctly
        and have the expected default values
        """
        dat = IndustryData()
        self.assertEqual(0, dat.num_areas)
        self.assertEqual(0, dat.total_annual_wages)
        self.assertEqual(["", 0], dat.max_annual_wages)
        self.assertEqual(0, dat.total_estabs)
        self.assertEqual(["", 0], dat.max_estabs)
        self.assertEqual(0, dat.total_emplvl)
        self.assertEqual(["", 0], dat.max_emplvl)

    def test_add_record(self):
        dat = IndustryData()
        dat.add_record(self.record0, self.areas)
        self.assertEqual(1, dat.num_areas)
        self.assertEqual(59925, dat.total_annual_wages)
        self.assertEqual(["TEST AREA A", 59925], dat.max_annual_wages)
        self.assertEqual(2, dat.total_estabs)
        self.assertEqual(["TEST AREA A", 2], dat.max_estabs)
        self.assertEqual(1, dat.total_emplvl)
        self.assertEqual(["TEST AREA A", 1], dat.max_emplvl)

        dat.add_record(self.record1, self.areas)
        self.assertEqual(2, dat.num_areas)
        self.assertEqual(47076946, dat.total_annual_wages)
        self.assertEqual(["TEST AREA B", 47017021], dat.max_annual_wages)
        self.assertEqual(24, dat.total_estabs)
        self.assertEqual(["TEST AREA B", 22], dat.max_estabs)
        self.assertEqual(606, dat.total_emplvl)
        self.assertEqual(["TEST AREA B", 605], dat.max_emplvl)

    def test_tied_emplvl(self):
        dat = IndustryData()
        dat.add_record(self.tied_emplvl0, self.areas)
        dat.add_record(self.tied_emplvl1, self.areas)
        self.assertEqual(1554, dat.total_emplvl)
        self.assertEqual(777, dat.max_emplvl[1])
        self.assertEqual("Employment Level Area 0", dat.max_emplvl[0])

    def test_tied_estabs(self):
        dat = IndustryData()
        dat.add_record(self.tied_estabs0, self.areas)
        dat.add_record(self.tied_estabs1, self.areas)
        self.assertEqual(1554, dat.total_estabs)
        self.assertEqual(777, dat.max_estabs[1])
        self.assertEqual("Number Of Establishments Area 0", dat.max_estabs[0])

    def test_tied_wages(self):
        dat = IndustryData()
        dat.add_record(self.tied_wages0, self.areas)
        dat.add_record(self.tied_wages1, self.areas)
        self.assertEqual(1554, dat.total_annual_wages)
        self.assertEqual(777, dat.max_annual_wages[1])
        self.assertEqual("Wages Area 0", dat.max_annual_wages[0])
