#include "printlib.h"

int main() {
    int x;
    x = 42;
    println_int(x+y);
    return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 18: Undefined variable y
