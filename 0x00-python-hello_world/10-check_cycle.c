#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @head: linked list head pointer
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *temp = NULL;

	if (head == NULL)
		return (0);

	temp = head->next;
	while (temp)
	{
		if (temp->next == head)
			return (1);
		temp = temp->next;
	}

	return (0);
}
