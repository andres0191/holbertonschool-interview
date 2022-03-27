# (484) 0x1D. AVL Trees

### :white_check_mark: 0. Is AVL
Write a function that checks if a binary tree is a valid AVL Tree

* Prototype: `int binary_tree_is_avl(const binary_tree_t *tree);`
* Where `tree` is a pointer to the root node of the tree to check
* Your function must return 1 if tree is a valid AVL Tree, and 0 otherwise
* If tree is `NULL`, return 0

Properties of an AVL Tree:

* An AVL Tree is a BST
* The difference between heights of left and right subtrees cannot be more than one
* The left and right subtree each must also be a binary search tree

File(s): [`0-binary_tree_is_avl.c`](./0-binary_tree_is_avl.c)\
Compiled: `gcc -Wall -Wextra -Werror -pedantic binary_tree_print.c 0-main.c 0-binary_tree_is_avl.c -L. -lavl -o 0-is_avl`
