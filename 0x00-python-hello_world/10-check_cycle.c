#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @head: linked list head pointer
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle, -1 if it fails
 */
int check_cycle(listint_t *head)
{
	listint_t *slow = NULL, *fast = NULL;

	if (head == NULL)
		return (-1);

	slow = head->next;
	fast = head->next->next;
	while (fast)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
