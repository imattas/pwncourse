CC ?= gcc
CFLAGS ?= -Wall -Wextra -O0 -g -fno-stack-protector -fno-omit-frame-pointer -no-pie -Wno-format-security
all: challenge
challenge: challenge.c
	$(CC) $(CFLAGS) -o $@ $<
clean:
	rm -f challenge

