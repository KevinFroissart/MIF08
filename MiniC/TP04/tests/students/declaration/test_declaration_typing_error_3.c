#include "printlib.h"

int main() {
    int x;
    x = true;
    println_int(x);
    return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 4: type mismatch for x: integer and boolean
