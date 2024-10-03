# CS 1440 Project 3: Big Data Processing - Instructions

Previous Semester Statistics     | Fall 2023 | Spring 2024
--------------------------------:|:---------:|:---------------
Average Hours Spent              | 10.31     | 9.592 
Standard Deviation Hours         | 5.417     | 4.498 
% students thought this was Easy | 20.0%     | 15.9% 
... Medium                       | 43.0%     | 39.8% 
... Hard                         | 21.0%     | 20.5% 
... Too Hard/Did not complete    | 16.0%     | 23.9% 


**You may use AI tools** such as ChatGPT or GitHub Copilot to assist with code and documentation

*   If you do this, explain in your Software Development Plan *which* tools were used, *where* they were used, and *how* they were used
*   Use comments to *clearly* identify which portions of source code were written by the tool
*   Failure to document use of these tools will be regarded as a **violation of academic integrity** and I will pursue sanctions
    *   The same applies to any other resources from outside the class


**Grace Points**: If these tags are pushed to GitLab before 11:59 PM on the Monday before the due date, you will get up to **5 grace points** per tag:

*   `analyzed`
*   `designed`

To be eligible for grace points these tags must be on **separate commits**; they cannot be together.

*   [How to Do This Project](#how-to-do-this-project)
    *   [Phase 0: Requirements Analysis](#phase-0-requirements-analysis-tag-name-analyzed)
    *   [Phase 1: Design](#phase-1-design-tag-name-designed)
    *   [Phase 2: Implementation](#phase-2-implementation-tag-name-implemented)
    *   [Phase 3: Testing and Debugging](#phase-3-testing-and-debugging-tag-name-tested)
    *   [Phase 4: Deployment](#phase-4-deployment-tag-name-deployed)
    *   [Phase 5: Maintenance](#phase-5-maintenance)
*   [What We Look for When Grading](#what-we-look-for-when-grading)


## How To Do This Project

*   Beginning with this project you will use **Git tags** to mark your progress through the Software Development Process.
    *   Incorrectly spelled/capitalized tags are ignored.
    *   **If you tag a wrong commit**, or **incorrectly spell a tag** refer to `Using_Git/Intermediate_Git.md` in the lecture notes for instructions.


### Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change any code in this phase**

0.  Download [2023.annual.singlefile.zip](https://gitlab.cs.usu.edu/-/project/4145/uploads/867bb0b8820747854498b736acc636d1/2023.annual.singlefile.zip) from GitLab and unzip it into `data/USA_full/`
    *   **Do not obtain this file from anywhere else**; there is a chance the BLS will change it without warning, rendering your output different from the provided examples.
    *   A `.gitignore` file protects you from committing large CSV files into your repo.
    *   Get help if you somehow commit a huge file!
0.  Read and run the included [unit tests](./Running_Unit_Tests.md) to orient yourself with the project.
1.  Read the [Project Requirements](./Project_Requirements.md).
2.  Read the Bureau of Labor Statistics (BLS) documents that describe the Quarterly Census of Employment and Wages (QCEW) data that you will be working with:
    *   [QCEW Area Codes and Titles](https://data.bls.gov/cew/doc/titles/area/area_guide.htm)
    *   [QCEW Field Layouts](https://data.bls.gov/cew/doc/layouts/csv_annual_layout.htm)
    *   [QCEW Ownership Codes](https://data.bls.gov/cew/doc/titles/ownership/ownership_titles.htm)
    *   [QCEW Industry Codes and Titles](https://data.bls.gov/cew/doc/titles/industry/industry_titles.htm)
3.  **Do not change the source code in this phase of the project!**
    *   You will edit code in **Phase 2: Implementation**.
    *   In this phase your task is to *draft* the plan that you will follow when you get there.
4.  Take the **Starter Code Quiz** on Canvas.
    *   Do not worry if you can't answer all of the questions yet
    *   You can re-take the quiz as many times as you want before the project is due
5.  Fill out **Phase 0** in Plan.md; explain in your *own words* what the program does, how it does it, and what changes you expect to make.
6.  Track your time in Signature.md.
7.  **Tag** the last commit in this phase `analyzed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed before 11:59 PM on the Monday before the due date, you will receive up to 5 points back*


### Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change any code in this phase**

0.  Design your functions on paper; **don't rewrite the Python code yet**.
    *   In this phase sketch out your *pseudocode*.
    *   Do not paste Python code into Plan.md; when we want to see your code we will read the `.py` files.
    *   Walk through the pseudocode in your head, with a pad of paper or a whiteboard to convince yourself that your design will work.
1.  You may write *some* runnable Python code to test out your ideas.
    *   This is called *prototyping*, and is a normal part of the design process.
    *   Do not become too attached to your prototype!
    *   Be prepared to delete prototype code after this phase.
    *   It helps to *not* write prototype code in the same files as *real* code.
2.  You should be able to get 100% on the **Starter Code Quiz** by now.
3.  Fill out **Phase 1** in Plan.md.
    *   This will be the longest portion of the document.
4.  Track your time in Signature.md.
5.  **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed before 11:59 PM on the Monday before the due date, you will receive up to 5 points back*


### Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

0.  Prepare the [data sets](./data/README.md) for testing
    *   The USA Full data set is too large to include in this Git repository
    *   If you haven't already done so, download [2023.annual.singlefile.zip](https://gitlab.cs.usu.edu/-/project/4145/uploads/867bb0b8820747854498b736acc636d1/2023.annual.singlefile.zip) from GitLab
    *   **Do not obtain this file from anywhere else**; there is a chance the BLS will change it without warning, rendering your output different from the provided examples.
    *   Unzip it into the `data/USA_full/` directory
    *   A `.gitignore` file protects you from committing large CSV files.  Contact your instructor if one is somehow committed!
    *   Follow the instructions in each sub-directory to create smaller data sets for testing
    *   Data sets with `_reversed` names are identical to the corresponding `_complete` data sets save for one difference - they are created with `tac` instead of `cat`.  This reversal of their contents should make no difference to your program.  Use these data sets to ensure this is the case.
1.  Run `python demo/benchmark.py data/USA_full/` and note how long the program ought to run on your computer.
2.  By the end of this phase the program is runnable and all unit tests pass.
    *   Don't forget to **close all files** that were used by the program.
    *   Delete all of the *TODO* messages in the source code.
3.  Fill out **Phase 2** in Plan.md.
    *   As you work in this phase you may choose to deviate from the design you settled upon in the previous phase.  This is normal!
    *   Briefly explain what changed.
    *   Do not paste long passages of Python code in Plan.md.
    *   Your write-up for this phase may be very short.
4.  Track your time in Signature.md.
5.  **Tag** the last commit in this phase `implemented` and push it to GitLab.


### Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Your grade depends on how your program performs when run from the command line.  We don't use PyCharm to grade, so ensure your program runs correctly from the shell.

0.  Run your program against all data sets.
    *   Your submission will be graded with `USA_full` and a **special, crafted data set** that you have not seen.
    *   To ensure that your program gets full marks, test it thoroughly!
1.  Verify that all unit tests still pass.
2.  Fill out **Phase 3** in Plan.md.
    *   Describe the tests cases you ran, both unit tests and integration tests.
    *   Make note of the commands that you ran and what happened in the program.
3.  If you found bugs in this phase, explain what was wrong and how you fixed it.
4.  Track your time in Signature.md.
5.  **Tag** the last commit in this phase `tested` and push it to GitLab.


### Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

It is your responsibility to ensure that your program will work on your grader's computer.

*   Code that crashes and *cannot* be quickly fixed by the grader will receive **0 points** on the relevant portions of the rubric.
*   Code that crashes but *can* be quickly fixed by the grader (or crashes only *some* of the time) will receive, at most, **half-credit** on the relevant portions of the rubric.

The following procedure is the best way for you to know what it will be like when the grader runs your code:

0.  Review [How to Submit this Project](./How_To_Submit.md) and make sure that your submission is correct.
1.  **Tag** the last commit in this phase `deployed` and push it to GitLab.
2.  Push your code to GitLab, then check that all of your files, commits and **tags** appear there.
3.  Clone your project into a *different directory*, and re-run your test cases.
    *   Run `git log` and verify that all tags are present and on the correct commit.


### Phase 5: Maintenance

0.  Review your Plan.md and Signature.md one last time.
1.  Fill out **Phase 5** in Plan.md by answering the questions.
2.  Make one final commit and push your **completed** Software Development Plan and Signature to GitLab.
3.  Make sure that you are happy with your **Starter Code Quiz** score.
4.  Respond to the **Project Reflection Survey** on Canvas.




## What We Look for When Grading

**Total points: 110**

*   **Repository Structure (10 points)**
    *   The repository is a clone of the starter code
    *   The repository's GitLab URL follows the naming convention
    *   All required files and directories are in their expected locations
    *   `.gitignore` is correct and no forbidden files or directories are present
    *   Each of the 5 Git tags are present in the repository, placed on the right commits, and spelled correctly
        1.  `analyzed`
        2.  `designed`
        3.  `implemented`
        4.  `tested` (may be on the same commit as `implemented`)
        5.  `deployed` (may be on the same commit as `tested`)
    *   If you accidentally commit a huge CSV file, ask the instructor for help
*   **Quality Documentation (35 points)**
    *   Plan.md
        *   Each section is filled out with a convincing level of detail
        *   No code is pasted from the source files
*   **Time Management (5 points)**
    *   Signature.md contains accurate information about the time you spent on this project
        *   The time reported on the **TOTAL** entry is the sum of the daily entries
    *   The *TODO* message and the placeholder entries have been removed
*   **Code Quality (30 points)**
    *   All unit tests pass
    *   Original unit tests are left unchanged (additional new tests are permitted, but not required)
    *   Doc strings and comments match the code they describe
    *   Functions and Classes are organized into the correct modules
    *   No useless variables or constants are present
    *   No useless import statements are present
    *   Program *does not* import any modules **except**:
        *   `sys`
        *   `time`
        *   `typing`
        *   modules provided by the starter code
        *   new modules you created yourself
        *   [Why the csv module is not on the approved list](./Project_Requirements.md#can-i-use-pythons-csv-module)
    *   No import statement fail due to misspelling or incorrect capitalization.
        *   **Windows users** make sure that the capitalization of file names on GitLab match your `import` statements!
    *   No imports involve the `src.` package; this is the result of a PyCharm misconfiguration
    *   No external programs are called to do the work
        *   Do not use `os.system()`, `subprocess`, `pipes` or similar features.
        *   This is a pure Python program, not a shell script that leverages external programs.
        *   The Text Tools from the previous project are an external program.
    *   `eval()` or similar functions are not used; use `int()` to convert strings into numbers
    *   Data files are closed in ordinary situations
        *   In the event of an error, your program will display an error message and immediately exit without closing files
*   **Program Behavior (30 points)**
    *   Program doesn't crash unexpectedly
    *   User Interface meets requirements
        *   Bad user input is detected and custom error messages provide an appropriate amount of detail
        *   File input/output issues cause Python's default stack trace message to appear
    *   Output exactly matches the examples
    *   The program finishes in a *reasonable* amount of time
    *   No extraneous output is printed to `sys.stdout` (extra output printed to `sys.stderr` is permitted)
        *   All of the *TODO* messages have been removed
    *   The program completely relies on user input to locate files
        *   Hard-coded paths are not written into the program
        *   The program works no matter what directory it is started from
