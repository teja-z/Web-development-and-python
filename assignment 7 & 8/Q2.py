class Queue:
    def __init__(self):
        self.queue = []

    # Method to enqueue (add) an element to the queue
    def enqueue(self, element):
        self.queue.append(element)
        print(f"Element {element} enqueued.")

    # Method to dequeue (remove) an element from the queue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty. Cannot dequeue.")
        else:
            removed_element = self.queue.pop(0)  # Remove the first element
            print(f"Element {removed_element} dequeued.")

    # Method to display the current queue
    def display(self):
        if len(self.queue) == 0:
            print("The queue is empty.")
        else:
            print("Current queue:", self.queue)

# Main code to interact with the user
def main():
    queue = Queue()

    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue Element")
        print("2. Dequeue Element")
        print("3. Display Queue")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = int(input("Enter the element to enqueue: "))
            queue.enqueue(element)
        
        elif choice == 2:
            queue.dequeue()
        
        elif choice == 3:
            queue.display()
        
        elif choice == 4:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()