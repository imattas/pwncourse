#include <stdio.h>
#include <stdlib.h>

int main(void) {
    void *first = malloc(24);
    void *second = malloc(24);
    printf("first=%p second=%p\n", first, second);
    free(first);
    free(second);
    puts("Inspect chunk spacing and allocator state in GDB.");
    return 0;
}

