#include "printlib.h"

int main() {
    int x;
    x = 0;
    while("test"){
        println_int(1);
        x = x + 1;
    }

    return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 6 col 4: invalid type for while condition: string