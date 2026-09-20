CC ?= gcc
CFLAGS ?= -Wall -Wextra -O0 -g -fno-omit-frame-pointer -fno-stack-protector -no-pie
all: challenge
challenge: challenge.c
	$(CC) $(CFLAGS) -o $@ $<
clean:
	rm -f challenge

