class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def appendleft(self, data):
        node = Node(data)
        if self.head is None: #기존 노드가 없을 때
            self.head = node
        else: #기존 노드가 존재할 때
            node.next = self.head #next는 기존 노드로 설정
            self.head = node #기존 노드보다 앞에 만들었으니까 head를 새 노드로
        self.length += 1 #길이 + 1

    def append(self, data):
        node = Node(data)
        if self.head is None: #기존 노드가 없을 때
            self.head = node
        else:
            prev = self.head
            while prev.next:
                prev = prev.next
            prev.next = node
        self.length += 1

    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            node = self.head
            while node.next: #node.next is not None
                print(node.data, end = " → ")
                node = node.next
            print(node.data)




mylist = Linked_list()


for data in (1, 2, 3, 4):
    mylist.display()
    if data % 2: #홀수는 앞에 추가
        mylist.appendleft(data)
    else: #짝수는 뒤에 추가
        mylist.append(data)

