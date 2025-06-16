"""
This module provides a LinkedList data structure implementation.
"""

from typing import Any, Optional, Generic, TypeVar

T = TypeVar('T')  # Generic type variable

class LinkedList(Generic[T]):
    """
    A generic doubly linked list implementation.

    Attributes:
        head (Optional[_Node[T]]): The first node in the linked list.
        tail (Optional[_Node[T]]): The last node in the linked list.
        size (int): The number of nodes in the linked list.
    """

    class __Node(Generic[T]):
        """
        An internal class representing a node in the linked list.

        Attributes:
            data (T): The data stored in the node.
            next (Optional[_Node[T]]): The next node in the list, or None if this is the tail.
        """
        def __init__(self, data: T):
            self.data: T = data
            self.leftPtr: Optional[LinkedList.__Node[T]] = None
            self.rightPtr: Optional[LinkedList.__Node[T]] = None

        def __str__(self) -> str:
            return str(self.data)

    def __init__(self) -> None:
        """Initializes an empty linked list."""
        self.head: Optional[LinkedList._Node[T]] = None
        self.tail: Optional[LinkedList._Node[T]] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.size == 0

    def __len__(self) -> int:
        """
        Returns the number of elements in the linked list.

        Returns:
            int: The size of the list.
        """
        return self.size

    def append(self, data: T) -> None:
        """
        Adds an element to the end of the linked list.

        Args:
            data (T): The data to append.
        """
        new_node = self._Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # self.tail will never be None here due to is_empty check
            self.tail.next = new_node # type: ignore
            self.tail = new_node
        self.size += 1

    def prepend(self, data: T) -> None:
        """
        Adds an element to the beginning of the linked list.

        Args:
            data (T): The data to prepend.
        """
        new_node = self._Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert(self, index: int, data: T) -> None:
        """
        Inserts an element at a specific position in the linked list.

        Args:
            index (int): The position at which to insert the data.
                         0 <= index <= size.
            data (T): The data to insert.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not (0 <= index <= self.size):
            raise IndexError(f"Index {index} out of bounds for list of size {self.size}")

        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return

        new_node = self._Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None: # Should not happen due to index check
                raise RuntimeError("Unexpected state: current node became None during insert.")
            current = current.next
        
        # current is now the node before the insertion point
        # current will not be None here because index > 0 and index < self.size
        new_node.next = current.next # type: ignore
        current.next = new_node # type: ignore
        self.size += 1

    def search(self, data: T) -> bool:
        """
        Searches for an element in the linked list.

        Args:
            data (T): The data to search for.

        Returns:
            bool: True if the data is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def get(self, index: int) -> T:
        """
        Retrieves the element at a specific position in the linked list.

        Args:
            index (int): The position of the element to retrieve.
                         0 <= index < size.

        Returns:
            T: The data at the specified index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not (0 <= index < self.size):
            raise IndexError(f"Index {index} out of bounds for list of size {self.size}")

        current = self.head
        for _ in range(index):
            if current is None: # Should not happen due to index check
                 raise RuntimeError("Unexpected state: current node became None during get.")
            current = current.next
        
        # current will not be None here
        return current.data # type: ignore

    def delete(self, data: T) -> None:
        """
        Deletes the first occurrence of an element from the linked list.

        Args:
            data (T): The data to delete.

        Raises:
            ValueError: If the data is not found in the list.
        """
        if self.is_empty():
            raise ValueError(f"Data '{data}' not found in an empty list.")

        # If head node itself holds the data to be deleted
        if self.head and self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            if self.is_empty(): # If the list becomes empty
                self.tail = None
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None: # Data not found
            raise ValueError(f"Data '{data}' not found in the list.")

        # Unlink the node from linked list
        # prev will not be None here because head case is handled
        prev.next = current.next # type: ignore

        if current == self.tail: # If the deleted node was the tail
            self.tail = prev
        
        self.size -= 1
        if self.is_empty(): # If the list becomes empty after deletion
            self.tail = None # Ensure tail is None if head is None


    def delete_at_index(self, index: int) -> T:
        """
        Deletes the element at a specific position in the linked list.

        Args:
            index (int): The position of the element to delete.
                         0 <= index < size.

        Returns:
            T: The data of the deleted element.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if not (0 <= index < self.size):
            raise IndexError(f"Index {index} out of bounds for list of size {self.size}")

        deleted_data: T
        if index == 0:
            # self.head will not be None here due to index and size check
            deleted_data = self.head.data # type: ignore
            self.head = self.head.next # type: ignore
            if self.size == 1: # List becomes empty
                self.tail = None
        else:
            current = self.head
            # Iterate to the node *before* the one to be deleted
            for _ in range(index - 1):
                if current is None or current.next is None: # Should not happen
                    raise RuntimeError("Unexpected list state during delete_at_index.")
                current = current.next
            
            # current is the node before the target node
            # current.next is the target node, it won't be None
            node_to_delete = current.next # type: ignore
            deleted_data = node_to_delete.data
            current.next = node_to_delete.next # type: ignore

            if node_to_delete == self.tail: # If deleting the tail node
                self.tail = current
        
        self.size -= 1
        return deleted_data

    def reverse(self) -> None:
        """Reverses the linked list in-place."""
        if self.size <= 1:
            return # No need to reverse empty or single-element list

        prev_node: Optional[LinkedList._Node[T]] = None
        current_node = self.head
        self.tail = self.head # The old head becomes the new tail

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        self.head = prev_node # The last prev_node is the new head

    def __str__(self) -> str:
        """
        Returns a string representation of the linked list.

        Returns:
            str: String representation like "LinkedList: [data1 -> data2 -> data3]".
        """
        if self.is_empty():
            return "LinkedList: []"
        
        nodes_str: list[str] = []
        current = self.head
        while current:
            nodes_str.append(str(current.data))
            current = current.next
        return "LinkedList: [" + " -> ".join(nodes_str) + "]"

    def __repr__(self) -> str:
        """
        Returns an official string representation of the linked list.

        Returns:
            str: Representation like "LinkedList([data1, data2, data3])".
        """
        if self.is_empty():
            return "LinkedList([])"
        
        elements: list[Any] = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return f"LinkedList({elements})"

# Example Usage (optional, can be removed or put in a separate test file)
if __name__ == "__main__":
    my_list = LinkedList[int]()
    print(my_list)  # LinkedList: []
    print(f"Is empty? {my_list.is_empty()}") # True
    print(f"Length: {len(my_list)}") # 0

    my_list.append(10)
    my_list.append(20)
    my_list.prepend(5)
    print(my_list)  # LinkedList: [5 -> 10 -> 20]
    print(f"Length: {len(my_list)}") # 3

    my_list.insert(1, 7) # Insert 7 at index 1
    print(my_list)  # LinkedList: [5 -> 7 -> 10 -> 20]
    my_list.insert(0, 1) # Insert 1 at index 0 (prepend)
    print(my_list)  # LinkedList: [1 -> 5 -> 7 -> 10 -> 20]
    my_list.insert(5, 30) # Insert 30 at index 5 (append)
    print(my_list)  # LinkedList: [1 -> 5 -> 7 -> 10 -> 20 -> 30]
    print(f"Length: {len(my_list)}") # 6

    print(f"Get element at index 2: {my_list.get(2)}") # 7
    print(f"Search for 10: {my_list.search(10)}") # True
    print(f"Search for 99: {my_list.search(99)}") # False

    deleted_item = my_list.delete_at_index(1) # Delete 5
    print(f"Deleted item at index 1: {deleted_item}") # 5
    print(my_list)  # LinkedList: [1 -> 7 -> 10 -> 20 -> 30]

    my_list.delete(20) # Delete value 20
    print(my_list)  # LinkedList: [1 -> 7 -> 10 -> 30]

    print("Reversing list:")
    my_list.reverse()
    print(my_list) # LinkedList: [30 -> 10 -> 7 -> 1]
    print(f"Head: {my_list.head.data if my_list.head else None}, Tail: {my_list.tail.data if my_list.tail else None}")

    # Test delete on single element list
    single_list = LinkedList[str]()
    single_list.append("A")
    print(single_list)
    single_list.delete("A")
    print(single_list) # LinkedList: []
    print(f"Head: {single_list.head.data if single_list.head else None}, Tail: {single_list.tail.data if single_list.tail else None}")

    # Test delete_at_index on single element list
    single_list.append("B")
    print(single_list)
    deleted_val = single_list.delete_at_index(0)
    print(f"Deleted: {deleted_val}")
    print(single_list) # LinkedList: []
    print(f"Head: {single_list.head.data if single_list.head else None}, Tail: {single_list.tail.data if single_list.tail else None}")

    # Test reversing an empty list
    empty_list = LinkedList[int]()
    empty_list.reverse()
    print(empty_list) # LinkedList: []

    # Test reversing a single element list
    single_item_list = LinkedList[int]()
    single_item_list.append(100)
    single_item_list.reverse()
    print(single_item_list) # LinkedList: [100]
    print(f"Head: {single_item_list.head.data if single_item_list.head else None}, Tail: {single_item_list.tail.data if single_item_list.tail else None}")

    str_list = LinkedList[str]()
    str_list.append("apple")
    str_list.append("banana")
    str_list.append("cherry")
    print(repr(str_list)) # LinkedList(['apple', 'banana', 'cherry'])