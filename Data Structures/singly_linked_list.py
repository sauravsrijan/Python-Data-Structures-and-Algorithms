class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.node_ids = [] # keeps track of the nodes that are in the linked list, helpful when adding a node relative to another node, also helpful for determining length
    
    def __str__(self) -> str:
        """Returns the content of the linked list."""
        current_node = self.head
        data = tuple() # Using tuple because it uses less memory
        while current_node:
            data += current_node.next
            current_node = current_node.next
        else:
            return str(data)
    
    def append(self, data) -> None:
        new_node = Node(data)
        if self.node_ids == 0: # if the linked list is empty, add the first node
            self.head = new_node

        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            else:
                last_node.next = new_node
        
        self.node_ids.append(id(new_node))

    def prepend(self, data) -> None:
        self.head = Node(data, next_node=self.head)
        self.node_ids.append(id(self.head))
    
    def insert_after_node(self, node: Node, data):
        if not isinstance(node, Node):
            raise TypeError("Argument 1 is not a node.")
        elif id(node) not in self.node_ids:
            raise IndexError("Node not in linked list.")
        else:
            node.next = Node(data, next_node=node.next)
            self.node_ids.append(id(node.next))

    def insert_at_index(self, index: int, data) -> None:
        if index is not int:
            raise TypeError("Index must be an integer.")
        elif index == 0:
            self.prepend(data)
        else:
            node = self.head
            node_index = 0
            while node_index != index:
                # TODO: increment node_index and travel through llist