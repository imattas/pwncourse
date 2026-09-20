#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

struct item { char name[16]; void (*action)(void); };

void safe(void) { puts("safe action"); }
void win(void) { puts("flag{heap-leak-chain}"); }

int main(void) {
    struct item *item = malloc(sizeof *item);
    item->action = safe;
    printf("item=%p\n", (void *)item);
    free(item);
    struct item *replacement = malloc(sizeof *replacement);
    puts("replacement data:");
    if (read(0, replacement, sizeof *replacement) != sizeof *replacement) return 1;
    replacement->action();
    return 0;
}
