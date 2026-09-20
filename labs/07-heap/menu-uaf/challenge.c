#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char *item = NULL;
    char command[16];
    while (fgets(command, sizeof command, stdin)) {
        if (!strncmp(command, "alloc", 5)) { item = malloc(32); strcpy(item, "fresh"); puts("allocated"); }
        else if (!strncmp(command, "free", 4)) { free(item); puts("freed"); }
        else if (!strncmp(command, "edit", 4)) { fgets(item, 32, stdin); puts("edited"); }
        else if (!strncmp(command, "show", 4)) { printf("item=%s", item); }
        else if (!strncmp(command, "quit", 4)) break;
    }
    return 0;
}

