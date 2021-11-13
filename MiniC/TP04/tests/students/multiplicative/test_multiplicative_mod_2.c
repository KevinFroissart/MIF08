#include "printlib.h"

int main() {
    int x;
    x = 42;
    println_int(x % 8);
    return 0;
}

// EXPECTED
// 2
