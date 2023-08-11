# 큐의 특징은 선입 선출
# rear front로 표현한다.
# dequeue는 가장 먼저 들어간 자료를 꺼낸다.

# Queue 클래스 만들기
# 연결리스트는 head만 존재했지만 Queue는 front와 rear가 존재함으로 두 변수를 잘 이동시켜야 한다.

# 노드를 삽입시

# 빈큐라면 front, rear가 모두 첫 노드를 가르켜야 한다
# 빈큐가 아니라면 rear와 next가 모두 새 노드를 가르키게 한 뒤 rear를 새 노드로 이동

# 노드를 꺼낼 때
# 빈 큐가 된다면 front와 rear는 모두 None을 가르켜야 한다
# 큐에 노드가 남으면 front를 front의 next로 옮긴다.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        # 만일 front가 None이라면 -> 빈 큐라면
        if self.front is None:
            # 생성한 노드가 프론트이자 rear이다.
            self.front = self.rear = node
        #만일 빈큐가 아니라면  rear를 새 노드로 옮긴다
        else:
            # 기존 rear의 next가 새노를 가르키게 하고
            self.rear.next = node
            # 새 노드를 rear로 다시 정의한다.
            self.rear = node
        #dequeue는 front 부터 데이터를 꺼냅니다. (선입선출)
    def dequeue(self):
        # 만일 빈 큐라면
        if self.front is None:
            print("Empty Queue")
            return None
        node = self.front
        #만일 Queue에 한가지 node만 있어 front와 rear가 모두 한가지 노드를 가르키고 있다면
        if self.front == self.rear:
            # 프론트와 rear모두 None으로 바꿔버린다.
            self.front = self.rear = None
        else:
            # next는 rear쪽을 가르키고 있음으로 front의 next를 front로 선언하면 됩니다.
            self.front = self.front.next

    def is_empty(self):
        return self.front is None # Queue가 비어있는지 확인해서 비어있다면 True 아니면 False

if __name__ == "__main__":
    q = Queue()

    for i in range(3):
        q.enqueue(chr(ord("A") + i))
        print(f"Enqueue data = {q.rear.data}")
    print()

    while not q.is_empty():
        print(f"Dequeue data = {q.dequeue()}")