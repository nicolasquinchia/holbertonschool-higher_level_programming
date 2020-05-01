#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: address of the head of the linked list
 * @number: number to insert in the linked list
 *
 * Return: Address of the new node or null if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == '\0')
	{
		return ('\0');
	}
	new->n = number;
	if (*head == '\0' || temp->n == number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp->next != '\0' && temp->next->n <= number)
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;
	return (new);
}
