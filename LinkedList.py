"""
This module provides a LinkedList data structure implementation.
"""

class LinkedList():

    class __Node():

        def __init__(self, data):
            self.data = data
            self.leftPtr = None
            self.rightPtr = None

        def __str__(self) -> str:
            return str(self.data)

        def __lt__(self, other) -> bool:
            if not isinstance(other, self.__class__):
                return NotImplemented
            return self.data < other.data
    
        def __eq__(self, other):
            return not self.data < other.data and not other.data < self.data
        
        def __ne__(self, other):
            return self.data < other.data or other.data < self.data
        
        def __gt__(self, other):
            return other.data < self.data
        
        def __ge__(self, other):
            return not self.data < other.data
        
        def __le__(self, other):
            return not other.data < self.data

        def __hash__(self):
            return hash(self.data)


    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size: int = 0

    def __hash__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            next_node = current.rightPtr
            current = next_node
        return hash(elements)
        
    def sort(self):
        if self.size <= 1:
            return self

        # Extract elements into a Python list
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            next_node = current.rightPtr
            current = next_node
        
        # Sort the Python list
        # This relies on the elements' own __lt__ method.
        try:
            elements.sort()
        except TypeError as e:
            # This can happen if elements are not mutually comparable
            raise TypeError(f"Elements in the LinkedList are not mutually comparable for sorting: {e}")

        # Populate the linked list with sorted elements by updating data in existing nodes
        current = self.head
        for sorted_data_item in elements:
            if current is None: # Should not happen if logic is correct
                raise RuntimeError("List structure changed unexpectedly during sort or size mismatch.")
            current.data = sorted_data_item
            current = current.rightPtr
            
        return self
    

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def append(self, data) -> None:
        new_node = self.__Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # self.tail will never be None here due to is_empty check
            self.tail.rightPtr = new_node # type: ignore
            self.tail = new_node
        self.size += 1

    def prepend(self, data) -> None:
        new_node = self.__Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.rightPtr = self.head
            self.head = new_node
        self.size += 1

    def insert(self, index: int, data) -> None:
        if not (0 <= index <= self.size):
            raise IndexError(f"Index {index} out of bounds for list of size {self.size}")

        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return

        new_node = self.__Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None: # Should not happen due to index check
                raise RuntimeError("Unexpected state: current node became None during insert.")
            current = current.rightPtr
        
        new_node.rightPtr = current.rightPtr # type: ignore
        current.rightPtr = new_node # type: ignore
        self.size += 1

    def search(self, data) -> bool:
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.rightPtr
        return False

    def get(self, index):
        if not (0 <= index < self.size):
            raise IndexError(f"Index {index} out of bounds for list of size {self.size}")

        current = self.head
        for _ in range(index):
            if current is None: # Should not happen due to index check
                 raise RuntimeError("Unexpected state: current node became None during get.")
            current = current.rightPtr
        
        return current.data # type: ignore

    def delete(self, data) -> None:
        if self.is_empty():
            raise ValueError(f"Data '{data}' not found in an empty list.")

        if self.head and self.head.data == data:
            self.head = self.head.rightPtr
            self.size -= 1
            if self.is_empty(): # If the list becomes empty
                self.tail = None
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.rightPtr

        if current is None: # Data not found
            raise ValueError(f"Data '{data}' not found in the list.")

        prev.rightPtr = current.rightPtr # type: ignore

        if current == self.tail: # If the deleted node was the tail
            self.tail = prev
        
        self.size -= 1
        if self.is_empty(): # If the list becomes empty after deletion
            self.tail = None # Ensure tail is None if head is None


    def delete_at_index(self, index: int):
        if not (0 <= index < self.size):
            raise IndexError(f"Index {index} out of bounds for list of size {self.size}")

        if index == 0:
            # self.head will not be None here due to index and size check
            deleted_data = self.head.data # type: ignore
            self.head = self.head.rightPtr # type: ignore
            if self.size == 1: # List becomes empty
                self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None or current.rightPtr is None: # Should not happen
                    raise RuntimeError("Unexpected list state during delete_at_index.")
                current = current.rightPtr
            
            node_to_delete = current.rightPtr # type: ignore
            deleted_data = node_to_delete.data
            current.rightPtr = node_to_delete.rightPtr # type: ignore

            if node_to_delete == self.tail: # If deleting the tail node
                self.tail = current
        
        self.size -= 1
        return deleted_data

    def reverse(self) -> None:
        if self.size <= 1:
            return # No need to reverse empty or single-element list

        prev_node = None
        current_node = self.head
        self.tail = self.head # The old head becomes the new tail

        while current_node:
            next_node = current_node.rightPtr
            current_node.rightPtr = prev_node
            prev_node = current_node
            current_node = next_node
        
        self.head = prev_node # The last prev_node is the new head

    def __str__(self) -> str:
        if self.is_empty():
            return "[]"
        
        nodes_str: list[str] = []
        current = self.head
        while current:
            nodes_str.append(str(current.data))
            current = current.rightPtr
        return "[" + ", ".join(nodes_str) + "]"

    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"
        
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.rightPtr
        return f"{elements}"
    