#include <stdio.h>

int main(void) {
    puts("hello from an ELF process");
    puts("Inspect me with: file ./challenge; readelf -h ./challenge");
    return 0;
}

