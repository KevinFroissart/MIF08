#include "printlib.h"

int main() {
    
    bool n;
    n = true;
    if(!n) {
    println_int(1);
    }
    else {
    println_int(0);
    }
    
    return 0;
}

// EXPECTED
// 0
