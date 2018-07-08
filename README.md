# Overview
The operations on graph, such as DFS (Depth First Search), BFS (Breadth First Search) etc.

# DFS
## Implementation
Implement class Node and class Graph in a file named graph.py. Implement a directed un-weighted in your Graph class. Note, a path is represented as a list of nodes in order such as path from `Node A` to `Node C` via `Node B`:

```
[Node({'A',['B']}), Node({'B',['C','D']}), Node({'C',['E','F']})]
```

Note, that the `{'A',['B']}` is used to exemplify, in the program it would be represented as `[Node 1, Node 2, Node 3]`.

**All functions operate on and return** `Node` object, a list of `Nodes`, or `self`. The two exceptions are `__str__` and `print_path` methods that return specified string representation of `Node` object.

## Test cases
Constructs graphs and node dictionaries for testing. One way to simplify is to make them module level and reuse in various tests. The test runs each of the functions and produce result output. To run the test it has to be sufficient to call it in command line as:

```
PYTHONPATH=. python -m pytest -v test_graph.py
```
