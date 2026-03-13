from LinkedList import linked_list
linkedlist = linked_list()
print("--------------------------")
print("Linked List")
print("--------------------------")
while True:
    print("--------------------------")
    print("[1] Add front")
    print("[2] Add Tail")
    print("[3] Add at index")
    print("[4] Delete at index")
    print("[5] Delete by value")
    print("[6] Print")
    print("--------------------------")

    user_input = input("Select Choice: ")

    if user_input == "1":
        print("--------------------------")
        print("INSERT FRONT")
        print("--------------------------")
        value = input("Select value: ")
        linkedlist.add_front(value)
        print("--------------------------")
    elif user_input == "2":
        print("--------------------------")
        print("INSERT BACK")
        print("--------------------------")
        value = input("Select value: ")
        linkedlist.add_tail(value)
        print("--------------------------")
    elif user_input == "3":
        print("--------------------------")
        print("INSERT AT")
        print("--------------------------")
        value = input("Select value: ")
        print("Length: ",end="") 
        print(linkedlist.get_length())
        index = input("Select index: ")
        linkedlist.add_at(value, index)
        print("--------------------------")
    elif user_input == "4":
        print("--------------------------")
        print("DELETE AT")
        print("--------------------------")
        index = input("Select index: ")
        linkedlist.delete_by_index(index)
        print("--------------------------")
    elif user_input == "5":
        print("--------------------------")
        print("DELETE BY VALUE")
        print("--------------------------")
        value = input("Select value: ")
        linkedlist.delete_by_value(value)
        print("--------------------------")
    elif user_input == "6":
        print("--------------------------")
        linkedlist.print()
        print("--------------------------")
    elif user_input == "-1":
        quit