#include "printlib.h"

int main() {
    int y;
    if(true){
        if(true){
            y = 0;
            while(y < 3) {
                println_int(2);
                y = y + 1;
            }
        }
        println_int(1);
    } else {
        println_int(0);
    }

    return 0;
}

// EXPECTED
// 2
// 2
// 2
// 1