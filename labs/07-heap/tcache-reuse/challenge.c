#include <stdio.h>
#include <stdlib.h>

int main(void) {
    void *first = malloc(32);
    printf("allocated=%p\n", first);
    free(first);
    void *reused = malloc(32);
    printf("reused=%p\n", reused);
    free(reused);
    return 0;
}

