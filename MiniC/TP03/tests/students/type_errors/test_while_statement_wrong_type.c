#include "printlib.h"

int main()
{
    while(5+5) {}
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 5 col 4: invalid type for while condition: integer
