#            Copyright © 2024 DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it is not allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macramé, and warm (but
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
        areas = {
                "02016": "TEST AREA A",
                "31079": "TEST AREA B",
                }

        record0 = '"02016","2","611","75","0","2022","A","",2,1,59925,0,0,1257,65373,"",17.34,0.03,0.02,0.00,0.00,0.79,0.79,"N",0,0.0,0,0,0,0,0,0,0,0,0,0,0,0'.split(",")
        dat.add_record(record0, areas)
        self.assertEqual(1, dat.num_areas)
        self.assertEqual(59925, dat.total_annual_wages)
        self.assertEqual(["TEST AREA A", 59925], dat.max_annual_wages)
        self.assertEqual(2, dat.total_estabs)
        self.assertEqual(["TEST AREA A", 2], dat.max_estabs)
        self.assertEqual(1, dat.total_emplvl)
        self.assertEqual(["TEST AREA A", 1], dat.max_emplvl)

        record1 = '"31079","1","102","72","0","2022","A","",22,605,47017021,0,0,1494,77682,"",2.02,0.93,1.07,0.00,0.00,1.16,1.16,"",0,0.0,-41,-6.3,-712727,-1.5,0,0.0,0,0.0,73,5.1,3787,5.1'.split(",")
        dat.add_record(record1, areas)
        self.assertEqual(2, dat.num_areas)
        self.assertEqual(47076946, dat.total_annual_wages)
        self.assertEqual(["TEST AREA B", 47017021], dat.max_annual_wages)
        self.assertEqual(24, dat.total_estabs)
        self.assertEqual(["TEST AREA B", 22], dat.max_estabs)
        self.assertEqual(606, dat.total_emplvl)
        self.assertEqual(["TEST AREA B", 605], dat.max_emplvl)
