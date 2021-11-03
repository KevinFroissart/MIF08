# MiniC interpreter and typer
LAB3, MIF08 / CAP 2021-22


# Authors

FROISSART Kévin p2002504

# Contents

TODO for STUDENTS : Say a bit about the code infrastructure ...

# Howto

`make tests-interpret TEST_FILES='TP03/tests/provided/examples/test00.c'` for a single run
it should print 42

`make tests` to test all the files in `*/tests/*` according to `EXPECTED` results.

You can select the files you want to test by using `make tests TEST_FILES='TP03/**/*bad*.c'` (`**` means
"any number of possibly nested directories").

# Test design 

My tests are shared between four separate folders. 

A first set of tests to test all the operators. If they are printed correctly and if error messages are shown as expected,
in case of divisions by 0 for example.

A second set of tests to test the 'if' and 'while' statements.

A third set of tests to test the type errors on statements, operations and assigns.

Finally, a folder for assign tests.

# Design choices

TODO : explain your choices - explain the limitations of your implementation.

# Known bugs

TODO : document any known bug and limitations. Did you do everything asked for?
