"""
  1. Linked List Node/Traversal
  Write a function that takes in the head node of a linked list and prints the data of every node in the list.
  
  2. Print odd nodes
	Write a method called print_odd_nodes that prints the nodes with odd-numbered indices (1, 3, 5, …, etc.)

	3. Write a function that removes a node with a given value from a singly-linked list. It should return the head node. The function should take in two arguments:
	head — the head of a linked list
	value — a value that you want to remove
"""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_nodes(self, head):
		current = head

		while current:
			print(current.data)
			current = current.next

	def print_odd_nodes(self):
		curr = self.head
		index = 0

		while curr:
			if index % 2 != 0:
				print(curr.data)
			index += 1
			curr = curr.next

	def removes(self, head, value):
		if head.data == value:
			return head.next

		curr = head.next
		temp = head	
		while curr:
			if curr.data == value:
				temp.next = curr.next	
				break
			curr = curr.next		
			temp = temp.next	

		return head


