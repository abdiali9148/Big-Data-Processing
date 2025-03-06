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


def area_titles_to_dict(dirname):
    """
    This function locates a CSV file called `area-titles.csv` in
    the specified directory, and transforms it into a dictionary
    """
    areas = {}
    f = open(f"{dirname}/area-titles.csv")
    for line in f:
        fields = line.split(",", 1)
        fips = fields[0].strip('"')
        area = fields[1].strip().strip('"')
        if len(fips) == 5 and fips.isdigit() and not fips.endswith("000"):
            areas[fips] = area
    return areas



