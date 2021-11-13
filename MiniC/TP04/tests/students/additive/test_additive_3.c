#include "printlib.h"

int main() {
    int x;
    x = 42 + 8;
    println_int(x);
    return 0;
}

// EXPECTED
// 50
