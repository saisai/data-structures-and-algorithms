# -*- coding: UTF-8 -*-

'''
	Class to implement queue in Python

	Queue: A queue stores elements in a linear fashion such that they follow first-in-first-out(FIFO) order. The elements
	are added to the top of the queue and removed from the beginning of the queue. 

'''

class Node(object):

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.nextnode = None



class Queue(object):

	def __init__(self):
		self.first = None
		self.last = None

	def enqueue(self, data):
		'''
			Function to insert elements into a queue
		'''
		# TODO: This should be dynamic in the sense that it can take any class
		node = Node(data)

		if self.first is None:
			self.first = node
			self.last = node

		else:
			self.last.nextnode = node
			self.last = self.last.nextnode


	def deque(self):
		'''
			Function to delete elements from a queue
		'''
		if self.first is None:
			raise ValueError("Queue is empty")

		# print self.first.data, "is removed"
		temp = self.first
		self.first = self.first.nextnode

		return temp

	def isEmpty(self):
		'''
			Function to check if the queue is empty
		'''
		if self.first is None:
			return True

		return False

	def peek(self):
		'''
			Function to print the top of the queue
		'''
		if self.last is None:
			raise ValueError("No element is there in queue")

		return self.last.data
