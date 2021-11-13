#include "printlib.h"

int main() {
    int x;
    x = 0;
    while(x < 10){
        println_int(1);
        x = x + 1;
    }

    return 0;
}

// EXPECTED
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
// 1
