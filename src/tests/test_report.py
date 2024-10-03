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
from report import Report


class TestReport(unittest.TestCase):

    def test_initializer_year(self):
        """
        The year of the Report object can be set from a parameter to the initializer
        It defaults to 1999
        """
        self.assertEqual(2000, Report(2000).year)
        self.assertEqual(1980, Report(1980).year)
        self.assertEqual(-1, Report(-1).year)

    def test_str(self):
        """Report.__str__ returns a well-formatted report"""
        report = Report(2036)
        report.all.num_areas = 1337
        report.all.total_annual_wages = 13333337
        report.all.max_annual_wages = ["Trantor", 123456]
        report.all.total_estabs = 42
        report.all.max_estabs = ["Terminus", 12]
        report.all.total_emplvl = 987654
        report.all.max_emplvl = ["Anacreon", 654]

        report.soft.num_areas = 1010
        report.soft.total_annual_wages = 101001110111
        report.soft.max_annual_wages = ["Helicon", 110010001]
        report.soft.total_estabs = 1110111
        report.soft.max_estabs = ["Solaria", 11000]
        report.soft.total_emplvl = 100010011
        report.soft.max_emplvl = ["Gaia", 10110010]

        exemplar = """\
<+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>
<+>                     UNITED STATES OF AMERICA                     <+>
<+>                    BUREAU OF LABOR STATISTICS                    <+>
<+>             Quarterly Census of Employment and Wages             <+>
<+>                 Annual Report For The Year 2036                  <+>
<+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>

Statistics over all industries
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Number of FIPS areas in report       1,337

Total annual wages                   $13,333,337
Area with maximum annual wages       Trantor
Maximum reported wages               $123,456

Total number of establishments       42
Area with most establishments        Terminus
Maximum # of establishments          12

Total annual employment level        987,654
Area with maximum employment         Anacreon
Maximum reported employment level    654


Statistics over the software publishing industry
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Number of FIPS areas in report       1,010

Total annual wages                   $101,001,110,111
Area with maximum annual wages       Helicon
Maximum reported wages               $110,010,001

Total number of establishments       1,110,111
Area with most establishments        Solaria
Maximum # of establishments          11,000

Total annual employment level        100,010,011
Area with maximum employment         Gaia
Maximum reported employment level    10,110,010"""

        # In case there is a difference between the strings, this
        # parameter controls how much is displayed
        self.maxDiff = 3000
        self.assertEqual(exemplar, str(report))
