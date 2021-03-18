#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: The pointer to the head of list
 * Return: 0 if has no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	do {
		if (tortoise == hare)
			return (1);
		tortoise = tortoise->next;
		if (hare->next != NULL)
			hare = hare->next->next;
		else
			hare = NULL;
	} while (tortoise != NULL && hare != NULL);
	return (0);
}