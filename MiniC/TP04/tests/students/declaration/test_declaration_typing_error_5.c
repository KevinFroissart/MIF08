#include "printlib.h"

int main() {
    bool x;
    x = 3.1;
    return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 5 col 4: type mismatch for x: boolean and float
