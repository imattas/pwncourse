#include <stdio.h>
#include <unistd.h>

volatile unsigned short auth;
int main(void) {
    char input[128];
    printf("auth=%p\n", (void *)&auth);
    ssize_t n = read(0, input, sizeof(input) - 1);
    if (n <= 0) return 1;
    input[n] = 0;
    printf(input);
    if (auth == 0x1337) puts("flag{fmt-write}");
    return 0;
}
