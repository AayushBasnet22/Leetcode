class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.data = val
        self.next = next

class LinkedList(ListNode):
    def __init__(self, val = 0, next = None) -> None:
        super().__init__(val, next)
    
    def showLinkedList(self) -> None:
        current = self
        while current is not None:
            print(current.data, end = ' -> ')
            current = current.next
        print("None")

    def insertatBeginning(self, node: 'LinkedList') -> None:
        head = self
        new_node = node
        new_node.next = head
        head = new_node

    def insertatEnd(self, node: 'LinkedList') -> None:
        tail = self
        while tail.next != None:
            tail = tail.next
        tail.next = node
 
    def insertatPosition(self, node: 'LinkedList', val: int) -> None:
        current = self
        new_node = node
        while current.data != val:
            current = current.next
        if current == None:
            assert f'value not in the list'
        else:
            new_node.next = current.next
        current.next = new_node
        print('Succesfully inserted')
        

if __name__ == '__main__':
    # Creating the nodes
    node1 = LinkedList(10)
    node2 = LinkedList(20)
    node3 = LinkedList(30)
    node4 = LinkedList(40)

    # Inserting the nodes at the end
    node1.insertatEnd(node2)
    node1.insertatEnd(node3)
    node1.insertatEnd(node4)

    # Showing the linked list
    node1.showLinkedList()
    # node5 = LinkedList(50)
    # node1.insertatBeginning(node5)
    # node5.showLinkedList()
    # node5.insertatPosition(LinkedList(60), 10)
    # node5.showLinkedList()
