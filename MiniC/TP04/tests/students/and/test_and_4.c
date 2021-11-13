#include "printlib.h"

int main() {
    
    bool n;
    n = false;
    if(n && 1) {
    println_int(1);
    }
    else {
    println_int(0);
    }
    
    return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 7 col 7: invalid type for boolean operands: boolean and integer
