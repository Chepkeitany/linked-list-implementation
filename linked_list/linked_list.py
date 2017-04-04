from .node import Node

class LinkedList(object):
    """
    Class implementation of the LinkedList
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None

        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return "{}".format([e.elem for e in self])

    def __len__(self):
        return self.count()

    def __iter__(self):
        current = self.start
        while current is not None:
            yield current
            current = current.next
        raise StopIteration

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        else:
            current = self.start
            counter = 0
            while True:
                if counter == index:
                    return current.elem
                current = current.next
                counter += 1

    def __add__(self, other):
        new_list = self.__class__([elem.elem for elem in self])
        for el in other:
            new_list.append(el.elem)
        return new_list

    def __iadd__(self, other):
        for el in other:
            self.append(el.elem)
        return self

    def __eq__(self, other):
        a = self.start
        b = other.start

        while True:
            if not a and b or not b and a:
                return False
            elif not a and not b:
                return True
            elif a.elem != b.elem:
                return False
            a = a.next
            b = b.next

    def __ne__(self, other):
        return not self.__eq__(other)

    def append(self, elem):
        new_node = Node(elem)
        if not self.start:
            self.start = new_node
            self.end = self.start
            return self.start
        else:
            self.end.next = new_node
            self.end = new_node

    def count(self):
        counter = 0
        for elem in self:
            counter += 1
        return counter

    def pop(self, index=None):
        """
        1 - check if index is valid
        2 - when index is 0 
        3 - pop with numbered index
        """

        # Implementation 1
        current = self.start
        if current is None:
            raise IndexError

        elif index is not None and index >= len(self):
            raise IndexError()
        else:
            list_length = len(self)

        current = self.start
        if index is None:

            if current == self.end:
                element = self.end.elem
                self.start = None
                self.end = None
                return element
            else:
                counter = 0
                while (counter < list_length - 2):
                    current = current.next
                    counter += 1
                current.next = None

                return self.end.elem

        elif index == 0:
            element = self.start.elem
            self.start = self.start.next
            return element

        else:
            prevNode = self.start
            for i in range(index - 1):
                prevNode = prevNode.next

            val = prevNode.next.elem
            prevNode.next = prevNode.next.next

            return val