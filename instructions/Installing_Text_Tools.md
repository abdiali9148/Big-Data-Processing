# CS 1440 Project 3: Big Data Processing - Installing Your Text Tools

**You are not expected to spend more than a few minutes installing your text tools.  If you get stuck, just use the shell's built-in tools.**

You have created your own text processing tools, which increase your power as a programmer in two ways:

0.  You have gained knowledge about processing textual data.
1.  You have a suite of useful commands that let you process large amounts of text more easily than with an editor, spreadsheet, or other graphical tool.

You can use your own text tools to get a handle on your next project.  Or, you can use the "real" text tools that come with the Bash shell.  The choice is yours!

Each of the tools implemented in Project #2 directly corresponds to a classic Unix text-processing program.  These programs have more options than yours, and are likely faster.

On the other hand, your Text Tools have the advantage of being flexible: you can add to or change them as the need arises.  And they are *yours*!  For this reason you can make them available for use anywhere on your system.



## How To Install Your Text Tools

While you were working on Project #2 your current working directory (CWD) had to be `src/` to run `tt.py`.  Further, when you ran the program you had to type `python tt.py` to launch it.

This document explains how to "install" your Text Tools so that you can run `tt.py` from *anywhere* on your system without needing to also type `python` in the command line.


### What Shell Am I Using?

To learn which shell you are using, run this command:

```
$ echo $SHELL
```

If you're using Bash you will see a path that ends with the word `bash`, such as `/bin/bash`.  If your computer uses the Z Shell, you'll see something like `/bin/zsh`.


### Git+Bash Users: Update $PATH In ~/.bash_profile

In order for `bash` to find `tt.py` on your system, you need to add its location to the shell's search path.

0. Open a new terminal window
1. Change into the `src/` directory containing `tt.py`
2. Run `pwd` to print the absolute path of this directory
3. Open the file `~/.bash_profile` in a proper text editor (i.e. PyCharm, *not* Notepad or WordPad)
4. Add this line to the bottom of `~/.bash_profile`, replacing `<TEXTTOOLS_DIR>` with the path from step 3

```
PATH=<TEXTTOOLS_DIR>:$PATH
```

It is important to *not* insert any white space around the assignment operator `=`.  This is a syntax rule of the shell; extra white space makes the shell misinterpret the command.

If the path to `tt.py` reported by `pwd` contains spaces (e.g. because your Windows username contains spaces), you'll need to "escape" them by adding a single backslash `\` in front of each one.


#### Test It Out

0.  Open a new bash window
1.  Run `tt.py`.  You should see its usage message and not a "command not found" error.



### Bash users on Linux or WSL

*   Follow the above instructions, but edit the file `~/.bashrc` instead of `~/.bash_profile`
*   Open a new terminal to test your configuration.


### macOS And Zsh Users

*   If your primary shell is Zsh, follow the Bash procedure described above, instead making changes to the file `~/.zshrc`.
*   Open a new terminal to test your configuration.



## Using *Your* Text Tools

Using the program you wrote yourself is the ultimate computer nerd flex.

After installing your text tools and creating `startgrep`, you can slightly modify the commands in the associated `data/*/README.md` file so that you can utilize your own text tools instead of the built-in Unix text tools.

The following commands are listed in `data/UT_all_industries/README.md` to create the `UT_all_industries` data set.

    head -n 1 ../USA_full/2023.annual.singlefile.csv > header.csv
    grep '^"49' ../USA_full/2023.annual.singlefile.csv > dat.csv
    grep '"0","10"' dat.csv > trimmed.csv
    cat header.csv trimmed.csv > 2023.annual.singlefile.csv
    rm header.csv dat.csv trimmed.csv

Utilizing your installed `tt.py`, the following commands can be run instead.

    tt.py head -n 1 ../USA_full/2023.annual.singlefile.csv > header.csv
    tt.py startgrep '"49' ../USA_full/2023.annual.singlefile.csv > dat.csv
    tt.py grep '"0","10"' dat.csv > trimmed.csv
    tt.py cat header.csv trimmed.csv > 2023.annual.singlefile.csv
    rm header.csv dat.csv trimmed.csv

Note the addition of the `tt.py` command before `head`, `grep`, and `cat`. Also note that `grep '^"49'` was replaced with `startgrep '"49'`. As the existing UNIX `grep` tool supports Regular Expressions to use `^` to denote "Look for `"49` at the start of the line", we replace this functionality with the `startgrep` tool created in class (find the code in the lecture notes).



## Troubleshooting

### bash: tt.py: command not found

This error indicates that the directory containing `tt.py` is not correctly specified in your `PATH`.

*   Launch a new shell and try again.  The shell reads its startup file once upon startup; changes made to it don't automatically affect instances of shells that are already running.
*   Double-check the spelling of the directory containing `tt.py` within `~/.bash_profile` or `~/.zshrc`.
*   Unless you've moved things around, the path containing `tt.py` should end in `src`.
*   If the path to `tt.py` on your system contains spaces, make sure each is escaped with a backslash `\`.  As an example, see how I handled John Jacob Jingleheimer Smith's home directory in Git+Bash:
    ```
    PATH=/c/Users/John\ Jacob\ Jingleheimer\ Smith/cs1440/proj3/src:$PATH
    ```


### 'python': No such file or directory

Errors messages containing these words look like the following:

```
/usr/bin/env: 'python': No such file or directory
```

```
bash: /c/Users/user/Desktop/cs1440-falor-erik-proj3/src/tt.py: /usr/bin/env: bad interpreter: No such file or directory
```

The remedy is to update the shebang line in `tt.py`.  The first line of `tt.py`
looks like this:

```
#!/usr/bin/env python
```

This line tells the bash shell which programming language to run the contents of that file in.  The name "shebang" is short for "hash-bang" and refers to the first two characters of the file.

The shebang line I provided *should* work for most systems.  When it doesn't, you'll get one of the above error messages.  If this happens to you, replace my shebang line with the location of the Python interpreter on your system.

0.  Find your python interpreter by running `which python`.  If you need to specifically run your code with `python3`, use `which python3`.
1.  Replace the entire first line of `tt.py` with a new line that begins with `#!` followed by the path returned by `which`.  The result will look something like this if you're using Git+Bash on Windows: `#!/c/Users/user/AppData/Local/Programs/Python/Python39/python`



### stdout is not a tty

If you're a Git+Bash user you may see this error when you try to redirect the output of `tt.py` to a file instead of the screen.

Because of the way that Python interacts with the terminal installed by Git+Bash you may have created an alias for the `python` program that runs it with another program called `winpty`.  This enables you to use the Python REPL from the command line, but breaks the ability to redirect the output of your text tools to a file.

You can approach this problem in three ways:

0.  Suppress the `winpty` + `python` alias on an as-needed basis with a backslash.  Each time you run Python you have the choice to use `winpty` or not:

```bash
$ \python src/tt.py head -n 10 README.md > testfile
```

1.  Remove the alias from your terminal for the rest of the session.  You need do this only once each time you open a terminal window:

```bash
$ unalias python
$ python src/tt.py head -n 10 README.md > testfile
```

2.  Remove the alias from `.bash_profile` or `.zshrc` in your home directory.  You'll need to find and open that file in a proper text editor (such as Nano).  Whenever you want to run the Python REPL from the bash shell you'll need to remember to first type `winpty` before `python` to prevent it from hanging.
