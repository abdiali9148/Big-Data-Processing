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


from util import get_emplvl, get_estabs, get_wages


class IndustryData:
    """
    Contains statistics for a single industry.
    """

    def __init__(self):
        self.num_areas = 0
        self.total_annual_wages = 0
        self.total_estabs = 0
        self.total_emplvl = 0

        self.max_annual_wages = ["", 0]
        self.max_estabs = ["", 0]
        self.max_emplvl = ["", 0]

    def add_record(self, record, areas):
        self.num_areas += 1

        area_name = areas.get(record[0].strip('"'), "")

        wages = get_wages(record)
        estabs = get_estabs(record)
        emplvl = get_emplvl(record)

        self.total_annual_wages += wages
        self.total_estabs += estabs
        self.total_emplvl += emplvl

        if wages > self.max_annual_wages[1]:
            self.max_annual_wages = [area_name, wages]

        if estabs > self.max_estabs[1]:
            self.max_estabs = [area_name, estabs]

        if emplvl > self.max_emplvl[1]:
            self.max_emplvl = [area_name, emplvl]
