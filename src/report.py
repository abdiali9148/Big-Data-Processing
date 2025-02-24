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


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !! YOU DO NOT NEED TO EDIT THIS FILE TO COMPLETE THIS PROJECT !!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# If there is a problem with the appearance of your report,
# the problem lies elsewhere.

from industry_data import IndustryData


class Report:
    """
    Collect statistics across multiple industries.

    Provide a ToString method (__str__) so that everybody's report will be
    formatted identically.  Create an instance of the Report class and print it
    out.
    """

    def __init__(self):
        self.year = 2023
        self.all = IndustryData()
        self.soft = IndustryData()

    def __str__(self):
        """
        This is Python's equivalent to Java's toString method

        Returns a string that displays a nicely formatted report
        """
        return f"""\
<<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>>
<<<                     UNITED STATES OF AMERICA                     >>>
<<<                    BUREAU OF LABOR STATISTICS                    >>>
<<<             Quarterly Census of Employment and Wages             >>>
<<<                      Annual Report For {self.year}                      >>>
<<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>>

Statistics For All Industries
-----------------------------------------------------------------------
Number of FIPS areas in report       {self.all.num_areas:,}

Total annual wages                   ${self.all.total_annual_wages:,}
Area with maximum annual wages       {self.all.max_annual_wages[0]}
Maximum reported wages               ${self.all.max_annual_wages[1]:,}

Total number of establishments       {self.all.total_estabs:,}
Area with most establishments        {self.all.max_estabs[0]}
Maximum # of establishments          {self.all.max_estabs[1]:,}

Total annual employment level        {self.all.total_emplvl:,}
Area with maximum employment         {self.all.max_emplvl[0]}
Maximum reported employment level    {self.all.max_emplvl[1]:,}


Statistics For The Software Publishing Industry
-----------------------------------------------------------------------
Number of FIPS areas in report       {self.soft.num_areas:,}

Total annual wages                   ${self.soft.total_annual_wages:,}
Area with maximum annual wages       {self.soft.max_annual_wages[0]}
Maximum reported wages               ${self.soft.max_annual_wages[1]:,}

Total number of establishments       {self.soft.total_estabs:,}
Area with most establishments        {self.soft.max_estabs[0]}
Maximum # of establishments          {self.soft.max_estabs[1]:,}

Total annual employment level        {self.soft.total_emplvl:,}
Area with maximum employment         {self.soft.max_emplvl[0]}
Maximum reported employment level    {self.soft.max_emplvl[1]:,}"""

    def __repr__(self):
        """
        Idem, but for the REPL and debugger.
        Simply does the same thing as __str__()
        """
        return self.__str__()
