### Linked List

# This project is an implementation of a LinkedList in Python.
A `LinkedList` (https://en.wikipedia.org/wiki/Linked_list) is a linear data structure and is constructed as a "chain" of Nodes. We'll see in detail how Nodes work because they're the objects holding the LinkedList structure.


### Nodes
Node are simple Python objects that have two values:

* An element (any python object): `1`, `hello`, `[1, 2, 3]`
* And a reference to another Node (that can be None, if the node is not connected to any other Node)

They can be created in the following way:

```python
n1 = Node(12)  # next is None
n2 = Node(99)  # next is None
n3 = Node(37)  # next is None
```

We can create a "chain" of nodes by connecting each one of these nodes to their respective "next" nodes:

```python
n1.next = n2  # 12 -> 99
n2.next = n3  # 99 -> 37


### Setting up
Clone the repository
Create a `virtual environment` (https://python-docs.readthedocs.io/en/latest/dev/virtualenvs.html)
In the project root directory, run `pip install -r dev-requirements.txt`


### Running tests
Run `make test`

#### Running individual test cases
`test_operations.py` is the file name in the tests folder
`TestCalculatorOperations` is the class name
`test_add` is the function to test
Run `PYTHONPATH=. py.test tests/test_operations.py::TestCalculatorOperations::test_add`



### Check for compatibility across Python versions
Run `tox`