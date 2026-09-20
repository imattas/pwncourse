#include <unistd.h>
int main(void) { char buffer[32]; write(1, "input:\n", 7); read(0, buffer, 128); return 0; }

