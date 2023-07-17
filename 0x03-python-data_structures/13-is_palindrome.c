#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: pointer to head of the list
 * Return: 0 if not a palindrome, 1 if otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j, len;
	int *array;

	if (*head == NULL || head == NULL)
		return (1);

	current = *head;
	len = 0;
	while (current != NULL)
	{
		current = current->next;
		len++;
	}

	array = malloc(sizeof(int) * len);
	if (array == NULL)
		return (0);
	current = *head;
	i = 0;
	while (current != NULL)
	{
		array[i] = current->n;
		current = current->next;
		i++;
	}

	for (i = 0, j = len - 1; i < len / 2; i++, j--)
	{
		if (array[i] != array[j])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
