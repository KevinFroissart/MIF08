#include "printlib.h"

int main() {
    if(true){
        println_int(1);
    } else {
        println_int(0);
    }

    return 0;
}

// EXPECTED
// 1
