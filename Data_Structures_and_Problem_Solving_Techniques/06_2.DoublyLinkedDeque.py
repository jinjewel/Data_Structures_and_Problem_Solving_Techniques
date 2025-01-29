#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.19
#######################################

# 이중연결리스트의 응용 : 연결된 덱

# 연결된 덱을 이중연결리스트로 구현하는 이유
# 단순연결리스트로 구현한 덱에선 DeleteRear를 진행할 때 바로 후단의 링크를 알수가 없어 불가능하다. O(n)

# 이를 해결하기 위해 이중연결리스트를 사용한다.
# 이중연결리스트로 구현한 덱에서 후단의 링크를 바로 알수 있으므로 DeleteRear를 문제없이 사용할 수 있다. O(1)

# 이중연결리스트를 구현하기 위한 양방향 노드 믈래스 생성
class DNode:
    def __init__(self, elem, prev = None, next = None): # 전단과 후단의 링크는 일단 None로 디폴트 값을 설정한다.
        self.data = elem
        self.prev = prev # 전단의 링크
        self.next = next # 후단의 링크
        
# 이중연결리스트를 이용한 덱 구현      
class DoublyLinkedDeque:
    def __init__(self):
        self.front = None # 맨 앞에 있는 노드를 가리킨다.
        self.rear = None # 맨 뒤에 있는 노드를 가리킨다.
        
    def isEmpty(self): 
        return self.front == None
    
    def clear(self):
        self.front = self.front = None
        
    def size(self): # 스택의 항목수 계산
        node = self.front # 맨 앞에 있는 노드의 값을 새로운 공간(노드)에 저장한다.
        count = 0
        while not node == None: # node가 None이 아닐 때 까지
            node = node.next # 다음 노드로 이동
            count += 1 # count 증가
        return count # count 반환  
    
    def display(self, msg='LinkedQueue'): # 메세지를 출력(디폴트값을 미리 대입해 놓는다.)
        print(msg, end=" ") # 입력받은 값을 먼저 출력을 하고
        node = self.front # 맨 앞에 있는 노드의 값을 새로운 공간(노드)에 저장한다.
        while not node == None:
            print(node.data, end=" ")
            node = node.next # 다음의 노드로 링크를 옮긴다.
        print()
    
    def addFront(self, item): # 앞에서 입력
        # 입력되는 값과 맨 앞에 삽입되는 것이므로 전단은 None, 루단에 이어질 링크는 원래 맨 앞이였던 front를 대입한다.
        node = DNode(item, None, self.front) 
        if (self.isEmpty()): # 덱스가 비어있으면 원소가 하나밖에 없다는 뜻이다.
            self.front = self.rear = node # front와 rear의 링크를 자기자신으로 가리킨다.
        else: # 공백이 아니면, 값이 덱스에 들어있다는 뜻
            self.front.prev = node # 현재 front는 앞에서 두번째 노드이므로 첫번째 노드와 전단 링크를 연결한다.
            self.front = node # front에 새롭게 생성한 노드를 위치 시킨다.  
        
    def addRear(self, item): # 후단에서 입력
        # 입력되는 값과 맨 뒤에서 삽입되는 것이므로 후단은 None, 전단은 원래 맨 뒤에 있던 rear를 대입한다.
        node = DNode(item, self.rear, None) 
        if(self.isEmpty()): # 덱스가 비어있으면 원소가 하나밖에 없다는 뜻이다.
            self.front = self.rear = node # front와 rear의 링크를 자기자신으로 가리킨다.
        else: # 공백이 아니면, 덱스에 값이 들어있다면 
            self.rear.next = node # 현재 rear는 뒤에서 두번째 노드이므로 후단에 현재 맨 뒤 노드인 node를 연결한다.
            self.rear = node # rear에 현재 맨 뒤 노드인 node를 연결한다.
            
    def deleteFront(self): # 전단에서 삭제
        if not self.isEmpty(): # 덱스가 비어져 있지 않다면
            data = self.front.data # front에 있던 노드의 데이터를 출력
            self.front = self.front.next # front에 두번째 앞에 있던 노드(front.next)를 연결한다.
            if self.front == None: # 만약 전단 노드가 없다면, 즉 덱스에 아무 값도 없다면
                self.rear = None # rear도 None값을 대입
            else: # 덱스에 남아 있는 값이 있다면
                self.front.prev = None # 이제 앞에서 2번째 노드가 맨 앞의 노드가 되었으므로 front의 전단링크를 None로 바꾼다.
            return data # 값을 리턴
        
    def deleteRear(self): # 후단에서 삭제
        if not self.isEmpty(): # 덱스가 비어져 있다면 
            data = self.rear.data # 맨 후단의 데이터를 삽입
            self.rear = self.rear.prev # 맨 뒤에서 2번째로 있던 값에 rear를 배치한다.
            if self.rear == None: # 만약 후단 노드가 없다면, 즉 덱스에 아무 값도 없다면
                self.front = None # front도 None으로 설정
            else: # 덱스에 값이 들어있으면
                self.rear.next = None # 이제 뒤에서 2번째 노드가 맨 뒤에 노드가 되었으므로 rear의 후단링크를 None로 바꾼다. 
            return data # step4
            
# 본문
if __name__ == "__main__":
    dq = DoublyLinkedDeque()
    for i in range(9):
        if i%2 == 0: # 짝수는 뒤에서 입력
            dq.addRear(i)
        else: # 홀수는 앞에서 입력
            dq.addFront(i)
    
    dq.display('DoublyLinkedDeque :')
     
    for i in range(2): # 전단에서 삭제
        dq.deleteFront()
     
    for i in range(3): # 후단에서 삭제
        dq.deleteRear()
     
    dq.display('DoublyLinkedDeque :') 
    
    for i in range(9,14):
        dq.addFront(i)
     
    dq.display('DoublyLinkedDeque :') 
'''
DoublyLinkedDeque : 7 5 3 1 0 2 4 6 8 
DoublyLinkedDeque : 3 1 0 2 
DoublyLinkedDeque : 13 12 11 10 9 3 1 0 2 
'''
'''9대신 20으로 대입했을 경우
DoublyLinkedDeque : 19 17 15 13 11 9 7 5 3 1 0 2 4 6 8 10 12 14 16 18 
DoublyLinkedDeque : 15 13 11 9 7 5 3 1 0 2 4 6 8 10 12 
DoublyLinkedDeque : 13 12 11 10 9 15 13 11 9 7 5 3 1 0 2 4 6 8 10 12 
'''

