class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top:
            popped = self.top
            self.top = self.top.next
            return popped.value

    def is_empty(self):
        return self.top == None

    def peek(self):
        if self.top:
            return self.top.value

        raise AttributeError("No Bueno")


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if self.rear:
            self.rear.next = node

        self.rear = node

        self.front = self.front or self.rear

    def dequeue(self):
        if self.front:
            value = self.front.value
            self.front = self.front.next
            return value

    def peek(self):

        if not self.front:
            raise AttributeError()

        return self.front.value

    def is_empty(self):
        return self.front == None


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
