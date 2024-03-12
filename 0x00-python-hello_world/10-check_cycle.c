#include "lists.h"

/**
* check_cycle - checks if a linked list contains a cycle
* @list: linked list to check
*
* Return: 1 if the list has a cycle, 0 if it doesn't
*/
int check_cycle(listint_t *list)
{
		listint_t *w = list;
		listint_t *t = list;

		if (!list)
			return (0);

		while (w && t && t->l_next)
		{
			w = w->l_next;
			t = t->l_next->l_next;
			if (w == t)
				return (1);
		}

		return (0);
}
