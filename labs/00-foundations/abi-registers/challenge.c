#include <stdio.h>

__attribute__((noinline)) long add_three(long a, long b, long c) {
    return a + b + c;
}

int main(void) {
    printf("sum=%ld\n", add_three(10, 20, 12));
    puts("Break on add_three and inspect rdi, rsi, rdx on x86-64 System V ABI.");
    return 0;
}

