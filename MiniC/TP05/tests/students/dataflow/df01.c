#include "printlib.h"

int main() {
    
    int x, y;
    x = 2;
    if (x < 4){
        x = 4;
        if(x == 4)
            x = 6;
        else 
            while (x != 10)
                x = x + 1;
        while(x != 0)
            x = x - 1;
    }
    else
        x = 5;

    return 0;
}

// EXPECTED
// 1
