#!/usr/bin/env python3

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
import tests.test_area_titles
import tests.test_report
import tests.test_industry_data
import tests.test_util


suite = unittest.TestSuite()
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tests.test_area_titles.TestAreaTitles))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tests.test_report.TestReport))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tests.test_industry_data.TestIndustryData))
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(tests.test_util.TestUtil))

unittest.TextTestRunner(verbosity=2).run(suite)
