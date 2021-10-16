#include "printlib.h"

int main()
{
    println_int(10%3);
    println_int(10%10);
    return 0;
}

// EXPECTED
// 1
// 0