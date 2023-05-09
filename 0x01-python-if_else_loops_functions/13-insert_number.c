#include "lists.h"

/**
 * insert_node - Insert a number into a sorted singly linkedlist.
 * @head: pointer to the head of list.
 * @number: number to be inserted.
 * Return: 0 If  function fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new1;

	new1 = malloc(sizeof(listint_t));
	if (new1 == NULL)
		return (NULL);
	new1->n = number;

	if (node == NULL || node->n >= number)
	{
		new1->next = node;
		*head = new1;
		return (new1);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new1->next = node->next;
	node->next = new1;

	return (new1);
}
