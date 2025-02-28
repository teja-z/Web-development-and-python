class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    # Method to display the linked list
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to insert a new node at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to delete a node by value
    def delete(self, data):
        if self.head is None:
            print("The list is empty.")
            return
        # If the node to be deleted is the head
        if self.head.data == data:
            self.head = self.head.next
            print(f"Node with data {data} deleted.")
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                print(f"Node with data {data} deleted.")
                return
            current = current.next
        print(f"Node with data {data} not found.")

# Main code to interact with the user
def main():
    linked_list = linkedList()

    while True:
        print("\n--- Linked List Operations ---")
        print("1. Display Linked List")
        print("2. Insert Node")
        print("3. Delete Node")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            linked_list.display()
        
        elif choice == 2:
            data = int(input("Enter the value to insert: "))
            linked_list.insert(data)
            print(f"Node with value {data} inserted.")
        
        elif choice == 3:
            data = int(input("Enter the value to delete: "))
            linked_list.delete(data)
        
        elif choice == 4:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()