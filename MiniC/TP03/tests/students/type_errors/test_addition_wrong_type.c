#include "printlib.h"

int main()
{
    int x;
    float y;
    int z;
    x=55;
    y=30.0;
    z = (x + y);
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 10 col 9: invalid type for additive operands: integer and float