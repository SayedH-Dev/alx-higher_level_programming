#include "lists.h"

/**
  * check_cycle - function that check for cycles within a singly linked list
  * @list: pointer to the head of the linked list
  * Return: 0 if no cycle or 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	if (list == NULL || list->nNode == NULL)
		return (0);

	listint_t *tort = list;
	listint_t *hare = list->nNode;

	while (hare != NULL && hare->nNode != NULL)
	{
		if (tort == hare)
			return (1);

		tort = tort->nNode;
		hare = hare->nNode->nNode;
	}
	return (0);
}
