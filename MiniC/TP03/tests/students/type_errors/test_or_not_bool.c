#include "printlib.h"

int main()
{
    if(false || 5){}
    return 0;
}

// EXPECTED
// EXITCODE 2
// In function main: Line 5 col 7: invalid type for boolean operands: boolean and integer