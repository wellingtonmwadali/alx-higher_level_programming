#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - A singly linked list
 * @i: Integer in script
 * @pos:  pointer to the next node
 */
typedef struct listint_s
{
	int i;
	struct listint_s *pos;
} listint_t;

size_t print_listint(const listint_t *h);

listint_t *add_nodeint(listint_t **head, const int n);

void free_listint(listint_t *head);

int check_cycle(listint_t *list);

#endif
