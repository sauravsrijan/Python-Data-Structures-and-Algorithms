class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_ids = [] # keeps track of the nodes that are in the linked list, helpful when adding a node relative to another node, also helpful for determining length
    
    def __str__(self) -> str:
        """Returns the content of the linked list."""
        current_node = self.head
        data = tuple() # Using tuple because it uses less memory
        while current_node:
            data += (current_node.data,)
            current_node = current_node.next
        else:
            return str(data)
    
    def __repr__(self):
        return str(self)
    
    def __getitem__(self, key: int) -> Node:
        if (key is not int) or (key < 0) or (key >= len(self.node_ids)) or (len(self.node_ids) == 0):
            raise IndexError("linked list index out of range")
        elif key == len(self.node_ids) - 1: return self.tail
        elif key == 0: return self.head
        else:
            node = self.head.next
            index = 1
            while index != key:
                node = node.next
                index += 1
            else: # On index and key match, return node
                return node
    
    def append(self, data) -> None:
        """Adds (appends) a node to the end of the list."""
        new_node = Node(data)
        if not self.node_ids: # if the linked list is empty, add the first node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next, self.tail = new_node, new_node
        
        self.node_ids.append(id(new_node))

    def prepend(self, data) -> None:
        """Adds a node to the beginning of the list (prepend)."""
        self.head = Node(data, next_node=self.head)
        self.node_ids.append(id(self.head))
    
    def append_at_node(self, node: Node, data):
        """Inserts a new node after the given node."""
        if not isinstance(node, Node):
            raise TypeError("Argument 1 is not a node.")
        elif id(node) not in self.node_ids:
            raise IndexError("Node not in linked list.")
        else:
            node.next = Node(data, next_node=node.next)
            self.node_ids.append(id(node.next))

    def insert_at_index(self, index: int, data) -> None:
        """Inserts a node at the given index, if the index is out of range, then it appends it to the end."""
        if type(index) is not int:
            raise TypeError("Index must be an integer.")
        elif index == 0:
            self.prepend(data)
        elif index >= len(self.node_ids):
            self.append(data)
        else:
            # Not starting at head, because if index was 0, then we would've already replaced the head in the second if statement.
            node = self.head.next
            last_node = self.head
            node_index = 1
            while node_index != index:
                last_node = node
                node = node.next
                node_index += 1
            else: # Node indexes matched, so insert node
                last_node.next = Node(data,next_node=node)
                self.node_ids.append(id(last_node.next))
            
    def remove_node(self, data) -> None:
        """Removes a node that matches the given data."""
        node = self.head
        while node.next:
            if node.data == data: break # break if node data matches given data
            else: node = node.next
        else: # node not found
            raise ValueError("Data not in linked list")

        # node found
        