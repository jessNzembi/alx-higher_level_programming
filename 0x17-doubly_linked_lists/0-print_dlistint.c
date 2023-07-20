#include "lists.h"

/**
 * print_dlistint - prints the elements of a doubly linked list
 * @h: pointer to the head
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *head = malloc(sizeof(dlistint_t));
	size_t count = 0;

	if (!h || !head)
		return (0);
	head = h;
	while (head)
	{
		printf("%d\n", head->n);
		count++;
		head = head->next;
	}
	free((void *)head);
	return (count);
}
