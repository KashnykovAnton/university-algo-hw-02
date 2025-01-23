from collections import deque

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    queue = deque(s)
    
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

while True:
    print("\nMenu:")
    print("Enter a string to check if it is a palindrome")
    print("Enter 'exit' to exit the program")
    input_string = input("\nEnter the string: ")
    if input_string.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    
    if is_palindrome(input_string):
        print("String is a palindrome")
    else:
        print("String is not a palindrome")
