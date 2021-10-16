#include "printlib.h"

int main()
{
    if(5+5 == 9) {
        println_string("OK");
    } else {
        println_string("KO");
    }
    return 0;
}

// EXPECTED
// KO
