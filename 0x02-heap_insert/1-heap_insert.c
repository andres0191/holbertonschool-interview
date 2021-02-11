#include "binary_trees.h"

/*
 * function that inserts a value into a Max Binary Heap
 *
 * @root: is a double pointer to the root node of the Heap
 * @value: is the value to store in the node to be inserted
 * Return: return a pointer to the inserted node, or NULL on failure
 */

heap_t *heap_insert(heap_t **root, int value)
{
heap_t *node, *parent;
	if (!*root)
	{
		node = binary_tree_node(*root, value);
		*root = node;
		return (*root);
	}
	node = *root;

	while (node)
	{
		parent = node;
		if (node->n == value)
			return node_swap(node);
		if (value > node->n)
			node = parent->left;
		else
			node = node->right;
	}

	if (value > parent->n)
	{
		parent->left = binary_tree_node(parent, value);
		return (parent->left);
	}
	else
	{
		parent->right = binary_tree_node(parent, value);
		return (parent->right);
	}
}

/*
 * node_swap - Swaps node with larger node
 * @node: Pointer
 * Return: The new node
 */

heap_t *node_swap(heap_t *node)
{
	while (node && node->parent)
	{
		while (node->n > node->parent->n)
		{
			node = node->parent;
			node->n += node->parent->n;
			node->parent->n -= node->n;
			node->parent->n = node->n - node->parent->n;
		}
	}
	return (node);
}