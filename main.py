


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
        self.header = Item()
        self.trailer = Item()

    #Add specified item, items should be in order of priority, 1 being the most important, no repeated values
    def addItem(self, nm, pri, desc, due):
        new_item = Item(nm, pri, desc, due)

        #If the list is empty
        if(self.header.next == None):
            self.header.next =  new_item
            self.trailer.prev =  new_item

            new_item.prev = self.header
            new_item.next = self.trailer
        #If the list is not empty, Look for where the item will go, check every item in the list if the priority value already exists
        else:
            #Will iterate through the list
            tNode = self.header.next

            while(tNode != None):

                if tNode.priority >= new_item.priority:
                    #Add new node before current node
                    new_item.prev = tNode.prev
                    tNode.prev.next = new_item
                    tNode.prev = new_item
                    new_item.next = tNode
                    return
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
            raise Exception("The list is empty")
        else:
            tNode = self.header.next
            while(tNode != None):
                if tNode.name == item_nm:
                    tNode.prev.next = tNode.next
                    tNode.next.prev = tNode.prev
                    del tNode

                    return
                tNode = tNode.next
            raise Exception("Name was not found in the list")
        return
        
            



    #Updates the specified item, might make helper functions in order to do this once since I plan on making it prompt the user what they would like to change (Priority, Name, Description, Due date, ect)
    def updateItem(self):
        pass

    def printList(self):
        if self.header == None:
            raise Exception("The list is empty")
        else:
            tNode = self.header.next
            while(tNode != None):
                print(tNode.priority)
                tNode = tNode.next
        return


def main():
    to_do_list = ToDoList

    while(True):
        print("\n\n\n\n\n\n\n\n\n\n")
        answer = input("What would you like to do?\nAdd Item: A\nRemove Item: R\nPrint list: P\nClose out of program: C\nEnter response: ")
        if(answer == 'A'):
            nm = input("Enter the name of the item: ")
            pri = input("Enter the priority of the item: ")
            desc = input("Enter a decription of the item: ")
            due = input("Enter the due date of the item: ")
            to_do_list.addItem(nm, pri, desc, due)

        elif(answer == 'R'):
            nm = input("Enter the name of the item you want to remove: ")
            to_do_list.removeItem(nm)
            
        elif(answer == 'P'):
            to_do_list.printList()
        elif(answer == 'C'):
            break
        else:
            raise Exception("That is not a valid command: ")
    return 
    

if __name__ == "__main__":
    main()



