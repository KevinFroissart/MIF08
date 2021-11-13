#include "printlib.h"

int main() {
    if(4>=true){
   	println_int(1);
    } else {
   	println_int(0);
    }
    return 0;
}

// EXITCODE 2
// EXPECTED
// In function main: Line 4 col 7: invalid type for relational operands: integer and boolean
