# NotBasic

Not basic is a basic like interpreted language designed for education purposes.
Not basic has a similar line number based system similar to basic that allows for
the creation of simple programs that for beginners is easier to step through than
regular code.

## The rules

Not basic follows some pretty simple rules.

1. A line must always start with a line number.
2. A line must always contain an operation. I.e: "jmp" or "add"
3. All operations are in lowercase.
4. Operations don't change the value of any operated on variables. You need to use the `store` operation for that.
5. A not basic file has the extension .nob
6. A not basic file should end with a new line that contains "eof"

## The syntax

The syntax is written in the VM.py file but the general idea can be found by looking through the testing files.

## Comments

All not basic comments are delimited by a semicolon. I.E: "10 println "Hello, World!" ; This is a comment!

## Running a not basic program

Running not basic programs is quite simple. Firstly, navigate to the directory where the not basic main.py file i located in and secondly type: `py main.py ./path/to/file.nob` for example: `py main.py ./tests/rand.nob`
