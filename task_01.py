from queue import Queue
import random
import time

queue = Queue()

def generate_request():
    new_request = {
    'id': random.randint(1, 1000),
    'time': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    queue.put(new_request)

    print(f'New request: id - {new_request["id"]}, time - {new_request["time"]}')

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f'Processing request: id - {request["id"]}, time - {request["time"]}')
    else:
        print('Queue is empty.')

def show_queue():
    if not queue.empty():
        print('Queue:')
        for item in queue.queue:
            print(f'id - {item["id"]}, time - {item["time"]}')
    else:
        print('Queue is empty.')

while True:
    print("\nMenu:")
    print("1. Generate request")
    print("2. Process request")
    print("3. Show queue")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        generate_request()
    elif choice == '2':
        process_request()
    elif choice == '3':
        show_queue()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")