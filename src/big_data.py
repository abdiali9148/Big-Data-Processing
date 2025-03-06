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


import sys
import time

from report import Report
from area_titles import area_titles_to_dict
from util import record_matches_fips, record_is_all_industries, record_is_software_industry

if len(sys.argv) != 2:
    print("Usage: src/big_data.py DATA_DIRECTORY")
    sys.exit()

print("Reading the databases...", file=sys.stderr)
before = time.time()

datadir = sys.argv[1]
areas = area_titles_to_dict(datadir)

# Create an empty Report object
rpt = Report()

annual_file = f"{datadir}/2023.annual.singlefile.csv"
f = open(annual_file)
for line in f:
    record = line.split(",")
    if record_matches_fips(record, areas) and record_is_all_industries(record):
        rpt.all.add_record(record, areas)
    elif record_is_software_industry(record):
        rpt.soft.add_record(record, areas)


after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report
print(rpt)
