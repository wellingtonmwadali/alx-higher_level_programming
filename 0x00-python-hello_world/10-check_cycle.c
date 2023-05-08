#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - it is a  function that checks for if a single linked list has a cycle
 *
 * @list1: linked list to be checked
 *
 * Return: 1 if cycle is present in list, 0 if not
 */

int check_cycle(listint_t *list1)

{
	listint_t *slow = list1;
	listint_t *fast = list1;

	if (!list1)
		return (0);

	while (slow && fast && fast->next)
i	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
