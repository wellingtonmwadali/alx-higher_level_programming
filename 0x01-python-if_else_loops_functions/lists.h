#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - its a singly linked list
 * @num: integer
 * @next: point to next node
 * Description: a singly linkedlist node structure
 */
typedef struct listint_s
{
	int num;
	struct listin_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *aadd_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);
#endif
