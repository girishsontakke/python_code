class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def lengthlist(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertHead(self, newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
        else:
            tempNode = self.head
            self.head = newNode
            newNode.next = tempNode

    def insertAt(self, newdata, position):
        if position < 0 or position > self.lengthlist():
            print("Invalid Position")
            return
        if position == 0:
            self.insertHead(newdata)
            return
        newNode = Node(newdata)
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition is position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def insertEnd(self, newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def delHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked list is empty, deletion failed.")

    def delEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def delAt(self, position):
        if position < 0 or position >= self.lengthlist():
            print("Invalid position")
        if self.isListEmpty() is False:
            if position == 0:
                self.delHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentnode = self.head
        while currentnode:
            print(currentnode.data, end=' ')
            currentnode = currentnode.next


linkedlist = LinkedList()
# linkedlist.insertEnd('Mahendra')
linkedlist.insertEnd('Sontakke')
linkedlist.insertHead('Girish')
linkedlist.insertAt('Mahendra', 1)
linkedlist.insertAt('.', 3)
linkedlist.delEnd()
linkedlist.delAt(0)
linkedlist.printList()
