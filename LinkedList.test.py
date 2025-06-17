import LinkedList as ll

def main():
    my_list = ll.LinkedList()
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
    my_list.insert(0, 11) # Insert 1 at index 0 (prepend)
    print(my_list)  # LinkedList: [1 -> 5 -> 7 -> 10 -> 20]
    my_list.insert(5, 30) # Insert 30 at index 5 (append)
    print(my_list)  # LinkedList: [1 -> 5 -> 7 -> 10 -> 20 -> 30]
    print(f"Length: {len(my_list)}") # 6

    print("Sorted List:", my_list.sort())
    
    print("List Hash:", my_list.hash())

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
    single_list = ll.LinkedList()
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
    empty_list = ll.LinkedList()
    empty_list.reverse()
    print(empty_list) # LinkedList: []

    # Test reversing a single element list
    single_item_list = ll.LinkedList()
    single_item_list.append(100)
    single_item_list.reverse()
    print(single_item_list) # LinkedList: [100]
    print(f"Head: {single_item_list.head.data if single_item_list.head else None}, Tail: {single_item_list.tail.data if single_item_list.tail else None}")

    str_list = ll.LinkedList()
    str_list.append("apple")
    str_list.append("banana")
    str_list.append("cherry")
    print(repr(str_list)) # LinkedList(['apple', 'banana', 'cherry'])

if __name__ == "__main__":
    main()