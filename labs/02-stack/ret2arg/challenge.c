#include <stdio.h>
#include <unistd.h>

void win(long value) {
    if (value == 0x13371337) puts("flag{ret2arg}");
}

__attribute__((naked)) void pop_rdi_ret(void) {
    __asm__("pop %rdi; ret");
}

int main(void) {
    char buffer[64];
    puts("argument:");
    read(STDIN_FILENO, buffer, 240);
    return 0;
}
