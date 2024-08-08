class DoubleLinkedListNode:
    def __init__(self, data: any) -> None:
        # Initialize a new node with the given data
        self.data = data  # Store the data in the node
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

class DoubleLinkedList:
    def __init__(self) -> None:
        # Initialize an empty doubly linked list
        self.head = None  # Head of the list
        self.tail = None  # Tail of the list
        self.size = 0     # Size of the list

    def append(self, data: any) -> None:
        # Append a new node with the given data to the end of the list
        if data is None:
            raise ValueError("Data cannot be None")  # Raise an error if data is None

        node = DoubleLinkedListNode(data)  # Create a new node
        if self.head is None:
            # If the list is empty, set the new node as both head and tail
            self.head = node
            self.tail = node
        else:
            # If the list is not empty, link the new node to the tail
            self.tail.next = node  # Link current tail's next to the new node
            node.prev = self.tail   # Link new node's prev to current tail
            self.tail = node        # Update the tail to the new node
        self.size += 1  # Increase the size of the list

    def insert_after(self, prev_node: DoubleLinkedListNode, new_data: any) -> None:
        # Insert a new node with the given data after the specified previous node
        if prev_node is None:
            raise ValueError("Previous node cannot be None")  # Raise an error if prev_node is None

        new_node = DoubleLinkedListNode(new_data)  # Create a new node
        new_node.next = prev_node.next  # Set the new node's next to the next of prev_node
        prev_node.next = new_node  # Link prev_node's next to the new node
        new_node.prev = prev_node  # Link new node's prev to prev_node
        if new_node.next:
            new_node.next.prev = new_node  # Update the next node's prev pointer
        else:
            self.tail = new_node  # Update tail if we are inserting at the end
        self.size += 1  # Increase the size of the list

    def remove(self, key: any) -> None:
        # Remove the first node with the specified data
        current = self.head  # Start from the head of the list
        while current:
            if current.data == key:
                # Node to be deleted is found
                if current.prev:
                    current.prev.next = current.next  # Link previous node to next node
                else:
                    self.head = current.next  # Update head if needed
                if current.next:
                    current.next.prev = current.prev  # Link next node to previous node
                else:
                    self.tail = current.prev  # Update tail if needed
                self.size -= 1  # Decrease the size of the list
                return
            current = current.next  # Move to the next node
        raise ValueError(f"Node with data {key} not found")  # Raise an error if the node is not found

    def print_list(self) -> None:
        # Print the data of each node in the list starting from the head
        current = self.head  # Start from the head of the list
        while current:
            print(current.data)  # Print the current node's data
            current = current.next  # Move to the next node

    def print_list_reverse(self) -> None:
        # Print the data of each node in the list starting from the tail
        current = self.tail  # Start from the tail of the list
        while current:
            print(current.data)  # Print the current node's data
            current = current.prev  # Move to the previous node

    def __len__(self) -> int:
        # Return the size of the list
        return self.size  # Return the current size of the list

# Example usage
dll = DoubleLinkedList()  # Create a new doubly linked list

# Append some elements to the list
dll.append(10)
dll.append(20)
dll.append(30)

print("Initial list:")
dll.print_list()  # Print the current list
print(f"List size: {len(dll)}")  # Print the size of the list

# Insert 15 after the first node
dll.insert_after(dll.head, 15)
print("\nAfter inserting 15 after 10:")
dll.print_list()  # Print the updated list
print(f"List size: {len(dll)}")  # Print the updated size of the list

# Remove a node with the value 20
dll.remove(20)
print("\nAfter removing 20:")
dll.print_list()  # Print the list after removal
print(f"List size: {len(dll)}")  # Print the updated size of the list

# Print the list in reverse order
print("\nList in reverse:")
dll.print_list_reverse()  # Print the list in reverse
