# menu-uaf

Objective: trace a menu protocol, free an object, then observe that `edit` still dereferences the stale pointer. Under GDB, inspect the pointer before and after `free`; explain why this is a lifetime bug rather than automatically an arbitrary write.

