#include <stdio.h>
#include <unistd.h>
#include <sys/prctl.h>
#include <linux/seccomp.h>

int main(void) {
    puts("Before filtering, inspect the process and list the syscalls the program needs.");
    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) != 0) return 1;
    puts("no_new_privs=enabled");
    puts("Teaching fixture: reason about syscall constraints without changing the host.");
    return 0;
}

