#include "printlib.h"

int main() {
    int x;
    x = 0;
    while(false){
        println_int(1);
        x = x + 1;
    }

    return 0;
}

// EXPECTED