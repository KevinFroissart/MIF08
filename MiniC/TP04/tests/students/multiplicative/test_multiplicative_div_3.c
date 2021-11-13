#include "printlib.h"

int main() {
    int x;
    x = 42;
    println_int(x / -2);
    return 0;
}

// EXPECTED
// -21
