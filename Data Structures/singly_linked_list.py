class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_ids = [] # keeps track of the nodes that are in the linked list, helpful when adding a node relative to another node, also helpful for determining length
    
    def __len__(self):
        return len(self.node_ids)
    
    def __str__(self) -> str:
        """Returns the content of the linked list."""
        current_node = self.head
        data = () # Using tuple because it uses less memory
        while current_node:
            data += (current_node.data,)
            current_node = current_node.next

        return str(data)

    def __repr__(self):
        return str(self)

    def __getitem__(self, key: int) -> Node:
        """Returns nodes on given key (index), does not support negative indexing smaller than -1 or slices."""
        if (type(key) is slice): raise NotImplementedError("Slices have are not supported")
        if (type(key) is not int): raise TypeError("indices must be integers")

        pre_tests = (
            (key >= len(self.node_ids)), # index out of max range
            (key < 0-len(self.node_ids)), # index out of min range
            (len(self.node_ids) == 0) # linked list is empty
        )
        
        if any(pre_tests): raise IndexError("linked list index out of range")

        if key in (0, 0 - len(self.node_ids)): return self.head
        elif key in (-1, len(self.node_ids) - 1): return self.tail
        else: # if index is negative...
            node = self.head.next # Head was returned in first if statement, no need to start at head
            index = 1-len(self.node_ids) if key < 0 else 1 # Because head was returned, there is also no need to have index start at 0 or the min negative index
            while index != key:
                node = node.next
                index += 1

            return node # On index and key match, return node

    def __setitem__(self, key, value):
        """Replaces the node's data at index, 'key', with 'value'."""
        if type(key) is slice: raise TypeError("indices must be integers, not slices")
        self[key].data = value
    
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

        if id(node) not in self.node_ids:
            raise KeyError("Node not in linked list.")

        node.next = Node(data, next_node=node.next)
        self.node_ids.append(id(node.next))

    def insert_at_index(self, index: int, data) -> None:
        """Inserts a node at the given index, if the index is out of range, then it appends it to the end."""
        if type(index) is not int: raise TypeError("index must be an integer.")
        if index < 0: raise ValueError("index must be non-negative")
        
        if index == 0:
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

            # Node indexes matched, so insert node
            last_node.next = Node(data,next_node=node)
            self.node_ids.append(id(last_node.next))

    def remove_node(self, data) -> None:
        """Removes a node that matches the given data."""
        if len(self.node_ids) == 0: raise ValueError(f"Data {data} not in linked list")
        last_node = cur_node = self.head
        while cur_node.next:
            if cur_node.data == data: break # break if node data matches given data
            else:
                last_node = cur_node
                cur_node = cur_node.next
        else: # node NOT found
            raise ValueError(f"Data {data} not in linked list")
        # node found
        last_node.next = cur_node.next
        self.node_ids.remove(id(cur_node))
        cur_node.data = cur_node.next = None # GC will take care of it 
        
