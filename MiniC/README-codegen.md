# MiniC Compiler 
LAB4 (simple code generation), MIF08 / CAP 2021-22

# Authors

FROISSART Kévin p2002504

# Contents

TODO for STUDENTS : Say a bit about the code infrastructure ...

# Howto

`python3 MiniCC.py TP04/tests/provided/step1/test00.c --reg-alloc=naive`: launch the compiler and obtain a RISCV code with temp.

`make TEST_FILES="TP04/tests/provided/step1/*.c" tests-naive`: check expected and compile with the naive allocation.

`make TEST_FILES="TP04/tests/provided/step1/*.c" tests-notsmart`: check expected and compile with the naive allocation and the all in memory allocation.

# Test design 

Tests are divided in 10 different folder.
Each folder is named after the functionality it tests.
Each folder contains a set of tests to test the expected 
behavior of both well written code and bad written one.
The relational test folder contains 6 other folders to
test each type of Conditions.
Eventually, a single test file at the root of 
the tests/students folder tests the ouf of memory case.

# Design choices

TODO: explain your choices

# Known bugs

TODO: Bugs and limitations.

# Checklists

A check ([X]) means that the feature is implemented 
and *tested* with appropriate test cases.

## Code generation

- [X] Number Atom 
- [X] Boolean Atom
- [X] Id Atom 
- [X] Additive expression
- [X] Multiplicative expr
- [X] UnaryMinus expr
- [X] Or expression
- [X] And expression
- [X] Equality expression
- [X] Relational expression (! many cases -> many tests)
- [X] Not expression

## Statements

- [X] Prog, assignements
- [X] While
- [X] Cond Block
- [X] If
- [X] Nested ifs
- [X] Nested whiles

## Allocation

- [X] Naive allocation
- [X] All in memory allocation
- [X] Massive tests of memory allocation

