#include "printlib.h"

int main()
{
    println_float("test");
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 5 col 4: invalid type for println_float statement: string