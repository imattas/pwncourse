# Writeup: fmt-read

Root cause: `printf(input)` treats attacker-controlled bytes as the format specification. Primitive: information disclosure through conversion directives.

Chain: input → format parser → pointer disclosure → hypothesis about stack/register state. The safe repair is `printf("%s", input)`.

