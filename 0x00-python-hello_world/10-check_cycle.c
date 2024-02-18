#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle using Floyd's algorithm.
 * Return: 1 if a cycle is detected, 0 otherwise.
 * Prototype: int check_cycle(listint_t *list);
 * @list: A pointer to the head of the linked list.
 */

int check_cycle(listint_t *list)
{
	/* Pointers to traverse the list, one step and two steps at a time */
	listint_t *tortoise;
	listint_t *hare;

	/* A null list does not contain a cycle */
	if (list == NULL)
		return (0);

	/* Start both pointers at the head of the list */
	tortoise = list;
	hare = list;

	/* Loop through the list to find a cycle if present */
	while (hare != NULL && hare->next != NULL)
	{
		/* Tortoise advances by one node */
		tortoise = tortoise->next;
		/* Hare advances by two nodes */
		hare = hare->next->next;

		/* If tortoise and hare meet, a cycle exists */
		if (tortoise == hare)
		{
			/* A cycle is found, return true */
			return (1);
		}
	}
	/* Reaching here means no cycle was found, return false */
	return (0);
}
