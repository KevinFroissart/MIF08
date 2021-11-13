#include "printlib.h"

int main() {
    if(true){
        if(true){
            if(false) {
                println_int(3);
            } else {
                println_int(4);
            }
        }
        println_int(1);
    } else {
        println_int(0);
    }

    return 0;
}

// EXPECTED
// 4
// 1