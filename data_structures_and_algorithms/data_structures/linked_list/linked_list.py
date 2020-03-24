""""
LinkedList & Node Implementations
class-05:
    LinkedList class
        __init__
        insert
        includes
        __str__
    Node class
        __init__

class-06:
    LinkedList -
        append
        insert_before
        insert_after

class-07:
    LinkedList -
        kth_from_end
"""


class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self, sequence=None):
        self.head = None

        if sequence:
            for item in sequence:
                self.append(item)

    def insert(self, value):
        """
        Adds value to beginning (aka head) of list
        """
        self.head = Node(value, self.head)

    def includes(self, value):
        """
        returns True/False if value found in list
        """

        current = self.head

        while current:

            if current.value == value:
                return True

            current = current.next

        return False

    def __str__(self):
        """returns linked list in stringy form

        Returns:
            [string] -- e.g. ['apples'],['bananas'],
        """
        output = ""

        current = self.head

        while current:
            output += f"[{current.value}],"
            current = current.next

        return output

    def append(self, value):
        """"adds value to end of list"""

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

    def insert_before(self, value, new_value):
        """"inserts new_value before the given value"""

        current = self.head

        while current and current.next:
            if current.next.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return

            current = current.next

        raise TargetError(f"{value} not in list")

    def insert_after(self, value, new_value):
        """"inserts new_value before the given value"""

        current = self.head

        while current:
            if current.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return

            current = current.next

        raise TargetError(f"{value} not in list")

    def kth_from_end(self, k):
        """get value k spots from the end of linked list"""
        scout = self.head

        straggler = None

        ahead = 0

        while scout:

            if ahead == k:
                straggler = self.head
            elif ahead > k:
                straggler = straggler.next

            ahead += 1

            scout = scout.next

        if not straggler:
            raise IndexError

        return straggler.value


class Node:
    """
    Node for use in a Linked List
    """

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class TargetError(ValueError):
    pass
