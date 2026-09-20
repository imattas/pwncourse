#include <unistd.h>
int main(void) { char buffer[64]; read(0, buffer, 200); return 0; }

