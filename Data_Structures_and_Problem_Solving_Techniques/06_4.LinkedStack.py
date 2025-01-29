#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.19
#######################################

# 연결된 구조는 흩어진 데이터를 링크로 연결해서 관리한다.
# 용량이 고정되어 있지 않다.
# 중간에 자료를 삽입하거나 삭제하는 것이 용이하다.

# 노드 : 중간 다리 같은 역활을 하며, 데이터를 담을 데이터 필드와 링크를 담을 하나 이상의 링크 필드가 필요하다.
# 헤드포인터 : 시작부분의 링크를 담아두는 곳이다.

# 연결 리스트의 종류
# 단순 연결 리스트
# 원형 연결 리스트
# 이중 연결 리스트

# 단순연결 리스트의 응용 : 연결된 스택

# 노드 클래스 구현
class Node: # 단순연결리스트를 위한 노드 클래스
    def __init__(self, elem, link=None): # 생성자, 디폴트 인수 사용
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = link # 링트 생성 및 초기화

# 연결된스택 클래스 구현        
class LinkedStack:
    def __init__(self): # 생성자
        self.top = None # top 생성 및 초기화
        
    def isEmpty(self): # 공백상태 검사
        return self.top == None

    def clear(self): # 스택 초기화
        self.top = None

    def push(self, item): # 연결된 스택의 삽입연산
        n = Node(item, self.top) # 새로운 공간(노드)에 추가할 값과 시작링크를 대입한다.
        self.top = n # 시작링크를 새롭게 만든 공간에 연결해준다.
        
    def pop(self): # 연결된 스택의 삭제연산
        if not self.isEmpty(): # 공백이 아니면
            n = self.top # 현재 가장 위에 있는 데이터를 새로운 공간(노드)에 대입한다.
            self.top = n.link # 시작링크을 가장 위에 있던 데이터 다음의 링크로 걸어둔다.
            return n.data # 새로운 공간에 저장해둔 노드의 데이터를 리턴한다.

    def size(self): # 스택의 항목수 계산
        node = self.top # 시작 노드
        count = 0
        while not node == None: # node가 None이 아닐 때 까지
            node = node.link # 다음 노드로 이동
            count += 1 # count 증가
        return count # count 반환
    
    def display(self, msg='LinkedStack'):
        print(msg, end=" ")
        node = self.top # 시작노드를 새로운 공간(노드)에 저장한다.
        while not node == None: # 노드에 값이 있으면 반복
            print(node.data, end=" ") # 값을 출력
            node = node.link # 다음노드를 가리키는 링크를 노드에 대입한다.
        print()
        
    def peek(self): # 가장 위에 있는 값 반환
        if not self.isEmpty(): # 비어있지 않으면
            return self.top.data # 시작 노드의 데이터를 리턴
           
# 본문
if __name__ == "__main__" :
        
    odd = LinkedStack()
    even = LinkedStack()
 
    for i in range(10):
        if i%2 == 0:
            even.push(i)
        else:
            odd.push(i)
 
    even.display(' 스택 even push 5회: ')
    odd.display(' 스택 odd  push 5회: ') 
 
    print(' 스택 even peek: ', even.peek())
    print(' 스택 odd  peek: ', odd.peek()) 
 
    for _ in range(2):
        even.pop()
    for _ in range(3):
        odd.pop() 
 
    even.display(' 스택 even pop 2회: ')
    odd.display(' 스택 odd  pop 3회: ') 

'''
 스택 even push 5회:  8 6 4 2 0 
 스택 odd  push 5회:  9 7 5 3 1 
 스택 even peek:  8
 스택 odd  peek:  9
 스택 even pop 2회:  4 2 0 
 스택 odd  pop 3회:  3 1 
'''
