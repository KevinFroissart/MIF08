#include "printlib.h"

int main()
{
    bool x;
    bool y;
    bool z;
    z = (x < y);
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 8 col 9: invalid type for relational operands: boolean and boolean