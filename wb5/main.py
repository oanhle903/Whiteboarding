"""
  Linked List Node/Traversal
  
  Write a function that takes in the head node of a linked list and prints the data of every node in the list.
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
