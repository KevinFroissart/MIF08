#include "printlib.h"

int main() {
    int x;
    x = 42 - 2;
    println_int(x);
    return 0;
}

// EXPECTED
// 40
