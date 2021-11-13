#include "printlib.h"

int main() {
    if(7.0){
        println_int(1);
    } else {
        println_int(0);
    }

    return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 4 col 4: invalid type for if condition: float
