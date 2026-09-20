#include <stdio.h>
#include <unistd.h>

void target(long value) { if (value == 0x42424242) puts("flag{rop-call}"); }
__attribute__((naked)) void pop_rdi_ret(void) { __asm__("pop %rdi; ret"); }
int main(void) { char buffer[64]; puts("rop:"); read(0, buffer, 200); return 0; }
