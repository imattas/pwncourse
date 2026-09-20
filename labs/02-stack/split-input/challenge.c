#include <stdio.h>
#include <unistd.h>

void win(void) { puts("flag{split-input}"); }

int main(void) {
    char first[32];
    char second[64];
    puts("first:");
    read(STDIN_FILENO, first, sizeof first);
    puts("second:");
    read(STDIN_FILENO, second, 200);
    return 0;
}
