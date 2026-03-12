from LinkedList import linked_list
linkedlist = linked_list()

print("Linked List")
while True:
    print("[1] Add front")
    print("[2] Add Tail")
    print("[3] Add at index")
    print("[4] Print")

    user_input = input("Select Choice: ")

    if user_input == "1":
        value = input("Select value: ")
        print()
        linkedlist.add_front(value)
    elif user_input == "2":
        value = input("Select value: ")
        print()
        linkedlist.add_tail(value)
    elif user_input == "3":
        value = input("Select value: ")
        print()
        print("Length: ",end="") 
        print(linkedlist.get_length())
        index = input("Select index: ")
        print()
        linkedlist.add_at(value, index)
    elif user_input == "4":
        linkedlist.print()
    elif user_input == "-1":
        quit