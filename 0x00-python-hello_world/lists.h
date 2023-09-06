#ifndef LISTS_H
#define LISTS_H

/*libraries*/
#include <stdio.h>
#include <stdlib.h>

/*singly linked list node definition*/
/**
  * struct listint_t - singly linked list
  * @x: data stored in the node with type integer
  * @nNode: pointer to the next node
  */
struct listint_t
{
	int x;
	struct listint_t *nNode;
};

typedef struct listint_t listint_t;

/*function declaration*/
int check_cycle(listint_t *list);

#endif
