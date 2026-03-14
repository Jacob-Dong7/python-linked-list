from LinkedList import linked_list
from DoublyList import DoubleLinkedList
def main():
    while True:
        print("--------------------------")
        print("Linked List")
        print("--------------------------")
        print("[1] Simple Linked List")
        print("[2] Double Linked List")
        print("--------------------------")
        user_input = input("Select Option: ")
        if user_input == "1":
            simple()
        elif user_input == "2":
            double()
        elif user_input == "-1":
            print("Exiting...")
            exit()
        else:
            print("Select from available option")
            continue


def double():
    doublelist = DoubleLinkedList()
    print("--------------------------")
    print("DOUBLE LINKED LIST")
    print("--------------------------")
    while True:
        print("--------------------------")
        print("[1] Add front")
        print("[2] Add Tail")
        print("[3] Add at index")
        print("[4] Delete at index")
        print("[5] Delete by value")
        print("[6] Print")
        print("[7] Print Reverse")
        print("[8] Search by value")
        print("[9] Search by index")
        print("[10] Find minimum value")
        print("[11] Find maximum value")
        print("--------------------------")

        user_input = input("Select Choice: ")

        if user_input == "1":
            print("--------------------------")
            print("INSERT FRONT")
            print("--------------------------")
            value = input("Select value: ")
            doublelist.add_front(value)
            print("--------------------------")
        elif user_input == "2":
            print("--------------------------")
            print("INSERT BACK")
            print("--------------------------")
            value = input("Select value: ")
            doublelist.add_back(value)
            print("--------------------------")   
        elif user_input == "3":
            print("--------------------------")
            print("INSERT AT")
            print("--------------------------")
            value = input("Select value: ")
            print("Length:", doublelist.get_length())
            index = input("Select index: ")
            doublelist.add_at(value, index)
            print("--------------------------")
        elif user_input == "4":
            print("--------------------------")
            print("DELETE AT")
            print("--------------------------")
            index = input("Select index: ")
            doublelist.delete_by_index(index)
            print("--------------------------")     
        elif user_input == "5":
            print("--------------------------")
            print("DELETE BY VALUE")
            print("--------------------------")
            value = input("Select value: ")
            doublelist.delete_by_value(value)
            print("--------------------------")     
        elif user_input == "8":
            print("--------------------------")
            print("SEARCH BY VALUE")
            print("--------------------------")
            value = input("Select value: ")
            doublelist.search_value(value)
            print("--------------------------")           
        elif user_input == "9":
            print("--------------------------")
            print("SEARCH BY INDEX")
            print("--------------------------")
            index = input("Select index: ")
            doublelist.search_index(index)
            print("--------------------------")  
            
        elif user_input == "10":
            print("--------------------------")
            print("MINIMUM")
            print("--------------------------")
            doublelist.min()
            print("--------------------------")
        elif user_input == "11":
            print("--------------------------")
            print("MAXIMUM")
            print("--------------------------")
            doublelist.max()
            print("--------------------------")
        elif user_input == "6":
            print("--------------------------")
            print("PRINT")
            print("--------------------------")
            doublelist.print()
            print("--------------------------")
        elif user_input == "7":
            print("--------------------------")
            print("REVERSE PRINT")
            print("--------------------------")
            doublelist.print_reverse()
            print("--------------------------")
        elif user_input == "-1":
            return         

def simple():
    linkedlist = linked_list()
    print("--------------------------")
    print("LINKED LIST")
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
            print("Length:", linkedlist.get_length())
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
            return


if __name__ == "__main__":
    main()