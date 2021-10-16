#include "printlib.h"

int main()
{
    int x;
    bool y;
    bool z;
    z = (x == y);
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 8 col 9: type mismatch for equality operands: integer and boolean