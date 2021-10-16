#include "printlib.h"

int main()
{
    string x;
    string y;
    string z;
    x="test";
    y="test";
    z = (x - y);
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 10 col 9: invalid type for additive operands: string and string