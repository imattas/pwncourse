#include <stdio.h>
#include <unistd.h>

void win(void) {
    puts("flag{ret2win}");
}

int main(void) {
    char buffer[64];
    puts("name:");
    read(STDIN_FILENO, buffer, 200);
    puts("done");
    return 0;
}
