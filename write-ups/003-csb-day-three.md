---
title: Day One
date: 06-06-19
Author: NC


---



# Day Three

## Review

Yesterday we covered the basics of bash in terms of navigating the file system, creating files and directories, deleting files and directories, and using output redirection to inject text into files.

### Bash Review

Some take aways from yesterday:

-   Use `pwd` to see what directory you are currently in
-   Use `cd [directory name]` to change directories
-   Use `cd ..` to go back to the parent of the directory you are in (up towards the root directory)
-   Use `cd ../../` with as many `../` as you need to go up as many levels as you need
-   Use `cd ~` to go to your home directory
-   Use `cd /` to go to the root directory
-   Use `mkdir [directory name]` to make directories use `-p` if you want 
-   Use `rm -rf` to recursively delete files and folders, but be careful with this command because it is easy whole folders 
-   Use `rmdir` to remove empty directories
-   Use `touch [filename]` to create files
-   Use `echo [string]` to print text to the terminal
-   Use `>` to inject text into files destructively, example: `ls > text.txt` will overwrite `text.txt` with the output of `ls` 
-   Use `>>` to append text to the end of a file, example `ls >> text.txt` will append the text from `ls` to the end of `text.txt` 

Relative and absolute paths:

-   You can use commands with **relative** or **absolute** paths:

    -   An **absolute** path is written all the way from the root directory example:

        ```bash
          /home/user-name/projects/bash-challenges
        # ^ the first slash is the root directory
        ```

    -   A **relative** path is written relative to the **current working directory**:

        ```bash
        # Assume you are currently in the home directory: ~/
          ./projects/bash-challenges
        # ^ the dot represents the current working directory
        ```

    -   The `~/` can also be used to create a **path** relative to your home directory:

        ```bash
        # Assume you are currently in the root directory, you could write a command using ~/ to 
        # run a command involving files or folders in the home directory.
           ~/projects/bash-challenges
        # ^ no matter which directory you are in this path will be relative to the home directory
        ```

### Tools Review

-   Most people have installed either Visual Studio Code or PyCharm - we will use these today, either is fine to use for development.
-   We looked at Slack and how to post code snippets on Slack
-   We looked at Github Gists and profile pages

### Outline

-   Python basics in the REPL - you can access the Python REPL by using your terminal and typing in `python`.

    **NOTE:** make sure you are using Python 3, you may need to use `python3` if you are on an Apple Computer.
