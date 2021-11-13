#include "printlib.h"

int main() {
    int x,y;
    x = 0;
    while(x < 2){
        y = 0;
        x = x + 1;
        while(y < 5) {
            println_int(1);
            y = y + 1;
        }
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

