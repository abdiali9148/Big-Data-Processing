# Software Development Plan

Phase 0: Requirements Analysis (tag name `analyzed`)
----------------------------------------------------
*(20% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.


Deliver:

*   [ ] Re-write the instructions in your own words.
    *   So the first thing I have to read all the data files and the QCEW files.
    *   I know that i have to make each of the 25 functions pass based on their unit test.
    *   
*   [ ] Explain the problem this program aims to solve.
    *   A good solution would be if all the tests pass, and if the report actually runs.
    *   From reading the project requirements i know how to work on most of the functions.
      * some functions say exactly what to do. for example on one, i just return and integer with the index i learn from
      *   one of the pages in the QCEW pages.
    *   Point out any challenges that you can foresee.
      *  As of right i don't know how i would work on the big_data.py module.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
        * Each of the functions wants to return something.
        * I have to keep reading the QCEW to find what each function wants to do.
        * in big_data.py it says if there is no argument, make it crash. so im assuming it wants me to
          * say a file each time.
*   [ ] Explain what form the program's output will take.
        *  When i run the src/big_data.py there must be a file after that.
        *  Once there is a file, it will run the report. All the unit tests must pass for the report to work.
*   [ ] **Tag** the last commit in this phase `analyzed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed before 11:59 PM on the Monday before the due date, you will receive up to 5 points back*


Phase 1: Design (tag name `designed`)
-------------------------------------
*(30% of your effort)*

**Important - do not change the starter code in this phase.**  Feel free to write prototype files and experiment in the REPL, but it's too early to work on the starter code now.

Deliver:

*   [ ] Pseudocode that captures how each function works in plain language.
    *   Pseudocode != Python.  Do not paste your finished source code into this part of the plan.
      *   Starting with util.py
        * for emplvl it says to extract the emplvl for a given year from the QCEW record.
          * looking into the QCEW record, the annual_avg_emplvl has a max length of 9.
            * ```python
                  i think when it says extract i will have to return something.
                  a record is "A line of text containing multiple fields separated by commas"
                      emplvl(record) Extracts the Annual average of monthly employment levels from a record.  Returns an integer.
                
                  return an integer of the 10th index in record. record[9] in python
                  ```
        * for estabs it says the same thing as emplvl but the quarterly establishment counts
          * im thinking i do the same thing but since the maximum in the QCEW records is 8 for estabs, 
            * i will return the integer value at the 8th index.
            * ```python
                return an integer of the 11th integer in record.
                    needs an integer because of said project requirements.
                    ```
        * for the get_fips, i had to look at the self.all_ind_10_good in the tests.
             * there are 2 indexes that could match the fips code. 0 and 10. 
          * since this function returns a string. ill probably use index 0 because it closely matches it.
            * ```python
                return the first index of record. so record[0]
                    no int because fips returns a string.
                    ```
        * get_wages.
          *  since i have planned the last 3, i have noticed a pattern with the test.
            * self.assertEqual(59925, get_wages(self.all_ind_10_good))
              * for every index in self.all_ind_10_good. the record[#] index has to be equal to that.
              * the 10th index in self.all_ind_10_good is 59925. so my output will be like this.
              * ```python
                    return an integer of the 11th integer in record.
                        int because wages returns an integer
                        ```
    * These last 3 only return True
        * record_is_all_industries
          * Records pertaining to "all industries" include a reportable FIPS area
            * this record has to return true if the industry code is 0 and ownership code is 10.
            * self.assertTrue(record_is_all_industries(self.all_ind_10_good))
              * this code is only true when the record is 0 and 10.\
              * this is true when record is the 2nd and 3rd indexes.
              
            * ```python
                    return true if the 2nd index of record is 0 and the 3rd index of record is 10.
                    ```
      * record_is_software_industry
        * same as all industries but returns true if the industry code is 513210 and ownership code is 5.
        * this one has a different list self.software_513210_good. so itll have the same code as all industries.
        * ```python
                return true if the 2nd index of record is 5 and the 3rd index is 513210
                ```
        
      * record_matches_fips
      ```python
           check to see if the get_fips record is in the area. if it is, return True
           ```
  
  * area_titles.py
        * the first thing i know about this is that i have to filter out some citys or countrys.
        * these are allowed and easily identified
        * The District of Columbia
          Puerto Rico
          Virgin Islands
          "Overseas Locations"
          "Multicounty, Not Statewide"
          "Out-of-State"
          and "Unknown Or Undefined" areas
  
       * The first thing im gonna do is open the file area-titles.csv.
         * since the parameters are dirname. im gonna start with opening the file with the directory name.
           * ```python
                file equal to directoryname,area-titles.csv
                open file.
                    go through each line
                        split each line into two fields
                        for each field, the first is the fips code, the second is the title
                        if the len of fips is 5 and its a digit and it does not end with 000.
                            add that title to the areas
                return the areas
          ```
    * industry_data.py
      * first this is the __init__(self) function.
        *  for the parameters, they all have to start with self.
        * Integers are initialized to 0 Strings are initialized to ""
        ``` python
        set self num_areas to be an integer so ill start it at 0.
        total_annual_wages is 0
        total_estabs is 0
        total_emplvl is 0
        ```
      * these 3 are lists
        ```python
        max_annual_wages stores an area and a number so it will be equal to ["",0]
        max_estabs stores the same thing
        max_emplvl stores the same thing.
       ```
    * add_record(self, record, areas)
      * the first thing i see in the test file is dat.num_areas has to be equal to 1.
        * so ill add one to it.
      ```python
      add one to self num_areas
      
      get the total of the wages, estabs, and emplv by importing and getting the total of the records.
      turn these all into variables.
      
      Update maximum annual wages if this record's wages are greater
      
      Update maximum establishments if this record's establishment count is greater.
      
      Update maximum employment level if this record's employment level is greater.
    ```
  * big_data
     ```python
        first thing in this file is to check if there is no file given.
            print a usage
        
        create the directory variable by using the second argument given.
        create the dictionary from the area titles dictionary. with the paramters datadir
        
        hard code the annual csv file
        open the file.
        read each line.
        * I see the annual file is a record seperated by commas so i am going to seperate it.
            split the record of each thing in the list by (",").
            if the fips match the record and the areas and the record is in all the industries
                then add the record to the report. all
            else if the software industry is in the record
                add the record to the report."soft" for software industries
        ```
  
*   [ ] Explain what happens in the face of good and bad input.
*  In good input, the report should print, in bad input it should crash or give a USAGE.
    *   As you think of specific examples, write them under **Phase 3** so you can run them as soon as the program is functional.
*   [ ] **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed before 11:59 PM on the Monday before the due date, you will receive up to 5 points back*


Phase 2: Implementation (tag name `implemented`)
------------------------------------------------
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] Working code in the `src/` folder.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
  *   One thing that was interesting was how i caught on to the tests and how both the annual files had
    * a lot of commas and a lot of quotes. I had to strip a lot of them.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.


Phase 3: Testing and Debugging (tag name `tested`)
--------------------------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   *   ill start by each function that gave me trouble.
      * get_fips
        * after playing with this function for a bit, the trouble i was having was that it was 
          * still keeping the quotes in the fips code. so i had to strip them using .strip('"')
      * record_is_all_industries and record_is_software_industry
        * the same thing for this, i had to strip the quotes out of "0" and "10"
      * area_titles_to_dict
        * the first thing i messed up was not adding a variable to create a dictionary.
          * this was the biggest thing because the function returns a dictionary.
        * also one big problem while testing was the fips and area needed to be stripped.
          * the fips needed to stripped of the quotes
          * the area needed to be stripped of every white space and the quotes they still had.
            * the area one confused me because i thought only the fips had quotes.
      * Industry_data and big_data worked easily.
    * the one thing messing up the output was in are_titles
      * fields = line.split(",")
        * line.split wants to split up everything instead of stoping after that ","
          * to get it to stop after only one split, i looked at the function.
            * one of its parameters was "max.split". i set this to 1 so it only split it once per line.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.


Phase 4: Deployment (tag name `deployed`)
-----------------------------------------
*(5% of your effort)*

Deliver:

*   [ ] **Tag** the last commit in this phase `deployed` and push it to GitLab. ok
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Look for all of the tags in the **Tags** tab.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


Phase 5: Maintenance
--------------------

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
          * I don't think any of my code is sloppily written. the only one i can think of is maybe industry_data.py
        *   Are there parts of your program which you aren't quite sure how/why they work?
          * I understood every part of it thanks to the unit tests.
        *   If a bug is reported in a few months, how long would it take you to find the cause?
          * pretty quick.
    *   Will your documentation make sense to...
        *   It was very hard getting the python code markups so that might be sloppily written.
          * it probably would only make sense to me.
    *   How easy will it be to add a new feature to this program in a year?
      * i would say a little more than medium. I would have to return back to this and read all of it and understand it all again.
    *   Will your program continue to work after upgrading...
      * i think it will still work because it is very simple.
          *   ...your computer's hardware?
          *   ...the operating system?
          *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Project Reflection Survey** on Canvas.
