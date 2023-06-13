#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i, j;

	if (head == NULL || *head == NULL)
		return (1);

	len = linked_list_len(*head);
	if (len % 2 != 0)
		return (0);

	for (i = 0, j = len - 1; i < (len / 2); i++, j--)
	{
		if (node_value(*head, i) != node_value(*head, j))
			return (0);
	}
	return (1);
}
/**
 * linked_list_len - how many nodes in a linked list
 *
 * @h: pointer of first node of a linked list
 *
 * Return: length of a listint_t list
 */
int linked_list_len(listint_t *h)
{
	int len = 0;
	listint_t *temp = NULL;

	temp = h;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	return (len);
}
/**
 * node_value - gives linked list node value at specific index
 *
 * @h: pointer of first node of a linked list
 * @indx: node index
 *
 * Return: node `n` value
 */
int node_value(listint_t *h, int indx)
{
	listint_t *temp = NULL;
	int i = 0;

	temp = h;
	while (i < indx)
	{
		temp = temp->next;
		i++;
	}
	return (temp->n);
}
