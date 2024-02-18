#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts an integer into a sorted singly linked list
 * @head: Double pointer to the head of the list
 * @number: The integer value to be inserted
 *
 * Description: This function creates a new node with the provided number
 * and inserts it into the list while maintaining the sorted order.
 * Return: A pointer to the new node, or NULL if memory allocation fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *cursor, *previous;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	cursor = *head;
	previous = NULL;


	while (cursor != NULL && cursor->n < number)
	{
		previous = cursor;
		cursor = cursor->next;
	}


	if (previous == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		previous->next = new;
		new->next = cursor;
	}

	return (new);
}

