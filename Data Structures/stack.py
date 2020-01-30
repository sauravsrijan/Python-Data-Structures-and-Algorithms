class Stack:
    def __init__(self):
        self.size = 0
        self.items = []

    def peek(self) -> object:
        """Returns the top element of the stack without deleting it."""
        return self.items[-1] if self.items else None

    def push(self, item) -> None:
        """Adds an element to the top of the stack."""
        self.items.append(item)
        self.size += 1

    def pop(self) -> object:
        """Returns and removes the top element of the stack."""
        if self.is_empty(): raise IndexError("Stack is empty")

        self.size -= 1
        return self.items.pop()

    def get_stack(self) -> list:
        """Returns all elements of the stack without clearing the stack."""
        return self.items.copy()

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return not self.items

    def clear(self) -> None:
        """Empties the stack."""
        self.items.clear()
        self.size = 0

    def __len__(self) -> int:
        return len(self.items)