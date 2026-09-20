# Writeup: menu-uaf

Root cause: `item` remains non-NULL after `free`, and both `edit` and `show` use it. Primitive: stale-pointer write followed by stale-pointer read. Chain: menu state → free → stale edit → observable reused bytes. Repair by setting `item = NULL` and rejecting edit/show when it is NULL.

