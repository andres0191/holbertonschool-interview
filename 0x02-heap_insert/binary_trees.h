#ifndef BINARY_TREES_H_
#define BINARY_TREES_H_

#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * struct of Binary trees
 *
 * @n: Integer in the node
 * @parent: Pointer to the parent node
 * @left: Pointer to the left node
 * @right: Pointer to the right node
 */
typedef struct binary_tree_s
{
	int n;
	struct binary_tree_s *parent;
	struct binary_tree_s *left;
	struct binary_tree_s *right;
} binary_tree_t;

typedef struct binary_tree_s heap_t;

void binary_tree_print(const binary_tree_t *);
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value);
heap_t *heap_insert(heap_t **root, int value);
heap_t *node_swap(heap_t *node);

#endif
