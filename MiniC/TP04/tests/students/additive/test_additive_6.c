#include "printlib.h"

int main() {
    println_int(50 ++ 10);
    return 0;
}

// EXITCODE 3
// EXPECTED
// line 4:20 extraneous input '+' expecting {'-', '!', '(', 'true', 'false', ID, INT, FLOAT, STRING}
