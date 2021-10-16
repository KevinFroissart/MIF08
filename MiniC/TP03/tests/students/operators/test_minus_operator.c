#include "printlib.h"

int main()
{
    println_int(5 - 10);
    println_int(5--5);
    println_int(5 - (-5));
    println_int(-5--5);
    return 0;
}

// EXPECTED
// -5
// 10
// 10
// 0