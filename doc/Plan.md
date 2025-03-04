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
    *   Describe important functions and classes in your program.  Include such details as:
        *   Names of functions/classes
        *   Parameter names and their types
        *   Types of data returned by functions
*   [ ] Explain what happens in the face of good and bad input.
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
    *   e.g. what you learned, what didn't go according to plan.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.


Phase 3: Testing and Debugging (tag name `tested`)
--------------------------------------------------
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
    *   Include a description of what happened for *each test case*.
    *   For any bugs discovered, describe their cause and remedy.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.


Phase 4: Deployment (tag name `deployed`)
-----------------------------------------
*(5% of your effort)*

Deliver:

*   [ ] **Tag** the last commit in this phase `deployed` and push it to GitLab.
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
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Project Reflection Survey** on Canvas.
