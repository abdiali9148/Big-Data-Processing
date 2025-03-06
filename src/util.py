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


def get_emplvl(record):
    """
    Extracts the annual average of monthly employment levels for a given
    year from a QCEW record
    """
    return int(record[9])


def get_estabs(record):
    """
    Extracts the annual average of quarterly establishment counts for a
    given year from a QCEW record
    """
    return int(record[8])


def get_fips(record):
    """
    Extracts a FIPS area code from a QCEW record
    """
    return record[0].strip('"')


def get_wages(record):
    """
    Extracts the sum of the four quarterly total wage levels for a given
    year from a QCEW record
    """
    return int(record[10])


def record_is_all_industries(record):
    """
    Predicate that takes a QCEW record and decides whether the record
    contains information about all industries under all types of
    ownership throughout the entire economy
    """
    return record[1].strip('"') == "0" and record[2].strip('"') == "10"


def record_is_software_industry(record):
    """
    Predicate that takes a QCEW record and decides whether the record
    contains information about privately owned software publishing firms
    """
    return record[1].strip('"') == "5" and record[2].strip('"') == "513210"


def record_matches_fips(record, areas):
    """
    Predicate that takes a QCEW record and dictionary of FIPS areas and
    decides whether the record contains information about a FIPS area in
    the dictionary
    """
    return get_fips(record) in areas
