#include <stdio.h>
#include <stdint.h>

int main(int argc, char **argv) {
    uintptr_t stack_value = (uintptr_t)&argc;
    printf("argc=%d argv=%p stack=%#lx\n", argc, (void *)argv, (unsigned long)stack_value);
    puts("Use GDB: break main; run alpha; info registers; x/4gx $rsp");
    return 0;
}

