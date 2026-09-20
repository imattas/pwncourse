CC ?= gcc
CFLAGS ?= -Wall -Wextra -O0 -g -fno-omit-frame-pointer
all: challenge
challenge: challenge.c
	$(CC) $(CFLAGS) -o $@ $<
clean:
	rm -f challenge

