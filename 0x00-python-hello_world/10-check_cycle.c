#include "lists.h"

/**
  * check_cycle - function that check for cycles within a singly linked list
  * @list: pointer to the head of the linked list
  * Return: 0 if no cycle or 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *tort;
	listint_t *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tort = list;
	hare = list->next;

	while (hare != NULL && hare->next != NULL)
	{
		if (tort == hare)
			return (1);

		tort = tort->next;
		hare = hare->next->next;
	}
	return (0);
}
