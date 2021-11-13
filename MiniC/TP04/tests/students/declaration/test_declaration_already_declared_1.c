#include "printlib.h"

int main() {
    int x;
    bool x;
    x = 42;
    println_int(x);
    return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 4: Variable x already declared
