#include "printlib.h"

int main()
{
    string x;
    bool y;
    y = !x;
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 7 col 8: invalid type for not expression: string