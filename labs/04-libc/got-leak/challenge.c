#include <stdio.h>
#include <unistd.h>

void win(void) { puts("flag{got-leak}"); }
int main(void) {
    char input[64];
    printf("puts=%p\n", (void *)puts);
    read(0, input, 160);
    puts("stage complete");
    return 0;
}
