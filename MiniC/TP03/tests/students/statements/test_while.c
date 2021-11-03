#include "printlib.h"

int main()
{
    int c;
    c=0;
    while(c<5) {
        c = c + 1;
        println_int(c);
    }
    return 0;
}

// EXPECTED
// 1
// 2
// 3
// 4
// 5
