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
print("TODO: import functions from the other modules")  # DELETE ME


print("TODO: If sys.argv[1] is not given, print a usage message and exit")  # DELETE ME

print("Reading the databases...", file=sys.stderr)
before = time.time()

print("TODO: Create a dictionary from 'sys.argv[1]/area-titles.csv'")  # DELETE ME
print("TODO: If accessing 'sys.argv[1]/area-titles.csv' fails, let your program crash here")  # DELETE ME
print("TODO: The FIPS dictionary should contain 3,463 pairs")  # DELETE ME

# Create an empty Report object
rpt = Report()

print("TODO: Fill in the report object with information taken from the annual singlefile CSV")  # DELETE ME
print("TODO: Read the unit tests to learn how to do that")  # DELETE ME

after = time.time()
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

# Print the completed report
print(rpt)

print("TODO: Did you delete all of the TODO messages?")  # DELETE ME
