#include "lists.h"

/**
 * is_palindrome - Verify if a linked list is palindrome
 * @head: (listint_t **) Head of the node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    int size_to_all = size_to_linkedList(*head);
    int size_to_half = (size_to_all / 2), step = 0;
    listint_t *left = *head, *right = NULL;
    size_t p = 0, q = 1;

    if (!size_to_all)
        return (1);

    for (; step < size_to_half; ++step)
    {
        right = *head;

        p = (size_to_all - step);
        /* Get the node of the right */
        for (q = 1; (q < p) && (right->next); ++j)
            right = right->next;

        if (left->n != right->n)
            return (0);

        left = left->next;
    }

    return (1);
}

/**
 * size_to_linkedList - Look amount of nodes
 * @head: Copy of the Head node
 *
 * Return: Length of the linked list
 */
int size_to_linkedList(listint_t *head)
{
    int i = 0;

    for (; head != NULL; ++i, (head = head->next))
        ;

    return (i);
}