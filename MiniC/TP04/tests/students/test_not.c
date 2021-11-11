#include "printlib.h"

int main() {
    bool b;
    b = false;
    if(!b){
   	println_string("OK");
    } else {
   	println_string("KO");
    }
    return 0;
}

// EXPECTED
// OK
