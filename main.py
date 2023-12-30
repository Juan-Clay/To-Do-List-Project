


#Will create a list object, might go ahead and make it a linked list to add a bit of difficulty and to have several properties per item 
#Doubly linked list cause it might come in handy when sorting


#"Node" class for this program
class Item:
    def __init__(self, nm = '', pri = 0, desc = '', due = ''):
        self.next = None
        self.prev = None

        self.name = nm
        self.priority = pri
        self.description = desc
        self.dueBy = due

#Will create the first nodde upon creation and house many different functions in order to give functionality to the list
class ToDoList:

    #Initialize list by creating header node, header node will not be an actual Item in the list
    def __init__(self):
        self.header = Item("head")
        self.trailer = Item("tail")

        self.header.next = self.trailer
        self.trailer.prev = self.header

    #Add specified item, items should be in order of priority, 1 being the most important, no repeated values
    def addItem(self, nm, pri, desc, due):
        new_item = Item(nm, int(pri), desc, due)

        #If the list is empty
        if(self.header.next == None):
            self.header.next =  new_item
            self.trailer.prev =  new_item

            new_item.prev = self.header
            new_item.next = self.trailer
        #If the list is not empty, Look for where the item will go, check every item in the list if the priority value already exists
        else:
            #Will iterate through the list, starts at first node that is not the header
            tNode = self.header.next

            while True:
                if tNode.priority >= new_item.priority:
                    #Add new node before current node
                    new_item.prev = tNode.prev
                    tNode.prev.next = new_item
                    tNode.prev = new_item
                    new_item.next = tNode
                    return
                else:
                    if tNode.next == None:
                        break
                    else:
                        tNode = tNode.next
            
            #If it reaches this point, the node goes at the end
            tNode.prev.next = new_item
            new_item.prev = tNode.prev
            new_item.next = tNode
            tNode.prev = new_item
        return


    #Remove specified item
    def removeItem(self, item_nm):
        if self.header == None:
            print("The list is empty\n\n")
        else:
            tNode = self.header.next
            while(tNode != None):
                if tNode.name == item_nm:
                    tNode.prev.next = tNode.next
                    tNode.next.prev = tNode.prev
                    del tNode
                    return
                tNode = tNode.next
            print("Item was not found in the list\n\n")
        return
        
            



    #Updates the specified item, might make helper functions in order to do this once since I plan on making it prompt the user what they would like to change (Priority, Name, Description, Due date, ect)
    def updateItem(self):
        pass



    def printList(self):
        if self.header.next == None or self.header.next.next == None:
            print("The list is empty\n\n")

        else:
            tNode = self.header.next
            while(tNode.next != None):
                print("Title: " + tNode.name)
                print("Priority: " + str(tNode.priority))

                #For desc and due date, if they are empty it does not print out the linea
                if tNode.description != '':
                    print("Description: " + tNode.description)

                if tNode.dueBy != '':
                    print("Due date: " + tNode.dueBy)
                print("\n\n")

                tNode = tNode.next
            print("\n\n")
        return


def main():
    #Creating the main list object and making a newline of 100 to clear the screen (Im lazy)
    to_do_list = ToDoList()
    print("\n" * 100)

    #Main loop of asking questions
    while(True):
        #asking all possible actions, and making the answer uppercase
        answer = input("What would you like to do?\nAdd Item: A\nRemove Item: R\nPrint list: P\nClose out of program: C\nEnter response: ")
        answer = answer.upper()
        if(answer == 'A'):
            print("\n" * 100)

            #Name
            nm = input("Enter the name of the item: ")
            #Input validation for name, must be non-empty
            while True:
                if nm == '':
                    nm = input("Name must be non-empty, please try again")
                else:
                    break

            #Priority
            pri = input("Enter the priority of the item: ")
            #Input validation for priority
            while True:
                if not pri.isnumeric():
                    pri = input("Not a number, please enter a number greater that 0: ")
                elif int(pri) < 1:
                    pri = input("Please enter a number greater that 0: ")
                else:
                    break

            #Description and due date, both optional, can be empty
            desc = input("Enter a decription of the item: ")
            due = input("Enter the due date of the item: ")
            to_do_list.addItem(nm, pri, desc, due)
            print("\n" * 100)

        elif(answer == 'R'):
            print("\n" * 100)
            nm = input("Enter the name of the item you want to remove: ")
            to_do_list.removeItem(nm)
            print("\n" * 100)
            
        elif(answer == 'P'):
            print("\n" * 100)
            to_do_list.printList()
        elif(answer == 'C'):
            break
        else:
            print("\n" * 100)
            print("That is not a valid command, please try again")
            print("\n\n")
    return 
    

if __name__ == "__main__":
    main()



