#include <stdio.h>
#include <unistd.h>

int main(void) {
    char input[128];
    puts("format:");
    ssize_t count = read(STDIN_FILENO, input, sizeof(input) - 1);
    if (count <= 0) return 1;
    input[count] = '\0';
    printf(input);
    putchar('\n');
    return 0;
}

