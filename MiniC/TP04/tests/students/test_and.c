#include "printlib.h"

int main() {
    
    bool n,m;
    n = true;
    m = false;
    if(n && m) {
    println_string("OK");
    }
    else {
    println_string("KO");
    }
    
    return 0;
}

// EXPECTED
// KO
