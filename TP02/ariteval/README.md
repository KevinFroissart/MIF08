# FROISSART Kévin p2002504 M1 Info 2020-2021

# LAB2, arithmetic expressions interpreter
MIF08, 2020-2021, Laure Gonnord & Matthieu Moy

# Content

This directory contains an interpreter for simple arithmetic
expressions like 5+3, for instance. The intepreter evaluates the
arithmetic expressions and prints their value on the standard
output.

# Usage

* `make` to generate AritLexer.py and AritParser.py (once)

* `python3 arit1.py <path/and/test/name>` to test a given file, for
 instance: 
 `python3 arit1.py tests/test01.txt`  should print `1+2 = 3`

* `make tests` to test on all tests files of the `testfile` directory

# Syntax of our language/restrictions

The syntax is the one textually given in the Lab2 sheet. 
Restriction : we did not implement minus nor unary minus.

# Design choices

The code can now make operations with the unary minus operator and the binary minus operator '-'.
I added the rule `MINUS e1=expr` at the very top of the `expr` rule in order to be able to make operations such as '-2' or '2--2'.
In addition to the MULT and PLUS rules I also added a MINUS rule for the binary operations.

# Known bugs

I didn't find any bugs with this implementation. I added 10 tests in order to test the unary and binary minus operators.
N/A
