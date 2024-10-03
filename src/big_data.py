#!/usr/bin/env python3

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

import sys
import time

from area_titles import area_titles_to_dict
from report import Report
from util import record_matches_fips, record_is_all_industries, record_is_software_industry


print("TODO: If sys.argv[1] is not given, print a usage message and exit")  # DELETE ME

print("Reading the databases...", file=sys.stderr)
before = time.time()

print("TODO: Create a dictionary from 'sys.argv[1]/area-titles.csv'")  # DELETE ME
print("TODO: If accessing 'sys.argv[1]/area-titles.csv' fails, let your program crash here")  # DELETE ME
print("TODO: The FIPS dictionary should contain 3,463 pairs")  # DELETE ME

print("TODO: Fill in the report using information from 'sys.argv[1]/2022.annual.singlefile.csv'")  # DELETE ME

# This is a demonstration of how to fill IndustryData objects with data
rpt = Report()

rpt.all.num_areas           = 1337
rpt.all.total_annual_wages  = 13333337
rpt.all.max_annual_wages    = ["Trantor", 123456]
rpt.all.total_estabs        = 42
rpt.all.max_estabs          = ["Terminus", 12]
rpt.all.total_emplvl        = 987654
rpt.all.max_emplvl          = ["Anacreon", 654]

rpt.soft.num_areas          = 1010
rpt.soft.total_annual_wages = 101001110111
rpt.soft.max_annual_wages   = ["Helicon", 110010001]
rpt.soft.total_estabs       = 1110111
rpt.soft.max_estabs         = ["Solaria", 11000]
rpt.soft.total_emplvl       = 100010011
rpt.soft.max_emplvl         = ["Gaia", 10110010]


after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report
print(rpt)

print("TODO: Did you delete all of the TODO messages?")  # DELETE ME
