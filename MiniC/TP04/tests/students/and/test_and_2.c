#include "printlib.h"

int main() {
    
    bool n,m;
    n = true;
    m = true;
    if(n && m) {
    println_int(1);
    }
    else {
    println_int(0);
    }
    
    return 0;
}

// EXPECTED
// 1
