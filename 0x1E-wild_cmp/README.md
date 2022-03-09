# 0x1E. Wild Compare


### Special Requirements
* You are not allowed to use loops of any kind.
* `ltrace` allowed functions: `write`, `printf`, `putchar`, `puts`
* `static` variables are not allowed

### Provided file(s)
* [`0-main.c`](./0-main.c)

---

## Mandatory Tasks

### :white_check_mark: 0. Wild Compare
Write a function that compares two strings and returns 1 if the strings can be considered identical, otherwise return 0.

* Prototype: `int wildcmp(char *s1, char *s2);`
* `s2` can contain the special character `*`.
* The special char `*` can replace any string (including an empty string)

File(s): [`0-wildcmp.c`](./0-wildcmp.c)\
Compiled: `gcc -Wall -pedantic -Werror -Wextra 0-main.c 0-wildcmp.c -o 0-wildcmp`

---

