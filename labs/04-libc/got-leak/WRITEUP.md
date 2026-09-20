# Writeup: got-leak

The diagnostic pointer is an information disclosure. A real chain would subtract the known `puts` offset from the matching local libc, assert page alignment, and use the resulting base to resolve a second symbol or gadget. Never mix libc versions.

