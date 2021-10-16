#include "printlib.h"

int main()
{
    println_string(8);
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 5 col 4: invalid type for println_string statement: integer
