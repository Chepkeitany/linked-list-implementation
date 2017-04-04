class Node(object):
    def __init__(self, elem, next=None):
        """ 
        Constructor, called every time a new object of the class is created.
        """
        self.elem = elem
        self.next = next

    def __str__(self):
        """
        Magic method to implement the native str() function
        :return: 
        """
        if self.next:
            return "Node({0}) > Node({1})".format(self.elem, self.next.elem)
        else:
            return "Node({0}) > /".format(self.elem)

    def __eq__(self, other):
        """
        Magic method to implement the equality operator(==)
        :param other: 
        :return: 
        """
        return self.elem == other.elem and self.next == other.next

    def __repr__(self):
        return str(self)