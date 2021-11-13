#include "printlib.h"

int main() {
    if(){
        println_int(1);
    } else {
        println_int(0);
    }

    return 0;
}

// EXITCODE 3
// EXPECTED
// line 4:7 mismatched input ')' expecting {'-', '!', '(', 'true', 'false', ID, INT, FLOAT, STRING}
