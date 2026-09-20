#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char *record = malloc(32);
    strcpy(record, "original");
    free(record);
    puts("The pointer is stale; inspect it in GDB before allocating again.");
    char *replacement = malloc(32);
    strcpy(replacement, "replacement");
    printf("stale-view=%s\n", record);
    free(replacement);
    return 0;
}

