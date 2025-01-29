#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.19
#######################################

# 원형연결리스트의 응용 : 연결된 큐

# 단순연결리스트로 구현한 큐 : 크기를 미리 정하고, front와 rear를 이용하여 구현
# 원형연결리스트로 구현한 큐 : 크기를 미리 정의할 필요가 없고, tail를 이용하여 rear와 front에 바로 접근할 수 있어 효율적이다.
# front -> tail.link
# rear -> tail
# 용량 제한이 없고, 삽입/ 삭제가 모두 O(1) 이다.

# 원형 연결 큐 구현

class Node: # 단순연결리스트를 위한 노드 클래스
    def __init__(self, elem, link=None): # 생성자, 디폴트 인수 사용
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = link # 링트 생성 및 초기화

class CircularLinkedQueue:
    
    def __init__(self): # 생성자 함수
        self.tail = None # tail : 유일한 데이터
        
    def isEmpty(self): # 공백상태 검사
        return self.tail == None 
    
    def clear(self): # 큐 초기화
        self.tail = None 
        
    def peek(self): # Peek연산
        if not self.isEmpty(): # 공백이 아니면
            return self.tail.link.data # front(tail.link)의 data를 반환
        
    def enqueue(self, item):
        # 일단 대입할 데이터를 담은 공간(노드)를 생성한다. 위치(링크)는 아직 모르므로 None로 가정한다.
        node = Node(item, None) 
        if self.isEmpty(): # 만약 큐가 비어져 있으면(값이 지금 대입한 값밖에 없으면)
            node.link = node # 새 공간의 링크를 자기자신으로 설정
            self.tail = node # 꼬리 노드를 새공간에 설정한다. 
        else:
            # 새공간이 새로운 꼬리노드가 될것이므로 새로운공간(노드)의 링크에 front(tail.link)를 연결한다.
            node.link = self.tail.link 
            self.tail.link = node # 원래 front를 가리키던 tail.link에 새롭게 생성된 노드를 연결해준다.
            self.tail = node # 꼬리 노드에 새로운 공간(노드)를 연결한다.
            
    def dequeue(self):
        if not self.isEmpty(): # 비워져있지 않으면 
            data = self.tail.link.data # front(tail.link)의 값을 출력해야하므로
            if self.tail.link == self.tail: # front(tail.link)와 rear(tail)가 같을경우, 즉 큐에 값이 하나밖에 없을 경우
                self.tail = None # 값을 반환하면 이제 큐에 감긴 원소가 업으므로 None
            else:
                # 원소가 2개 이상있다면, rear(tail)에 front(tail.link)의 다음 노드(tail.link.link)를 연결한다.
                self.tail.link = self.tail.link.link 
            return data # 처음에 저장해 놨던 값을 반환

    def size(self):
        if self.isEmpty(): # 공백 : 0반환
            return 0 
        else: # 공백이 아니면
            count = 1 # count는 최소 1
            node = self.tail.link # front(tail.link) 노드를 새로운 공간(노드)에 저장한다.
            while not node == self.tail: # node가 rear(tail)를 만날 때까지
                node = node.link # 노드를 차례대로 이동
                count += 1 # count 증가
            return count # 최종 count 반환
        
    def display(self, msg='CircularLinkedQueue'): # 메세지를 출력(디폴트값을 미리 대입해 놓는다.)
        print(msg, end=" ") # 입력받은 값을 먼저 출력을 하고
        if not self.isEmpty(): # 큐가 비어있지 않으면
            node = self.tail.link # front(tail.link) 노드를 새로운 공간(노드)에 저장한다.
            while not node == self.tail : # node가 rear(tail)를 만날 때까지
                print(node.data, end=" -> ") 
                node = node.link # 다음 노드로 이동
            # self.tail의 node는 비교에 의해 while문에 들어가지 못하므로 
            # 반복이 끝나고 한번더 출력을 진행해야한다.    
            print(node.data, end=" (fin) ") 
        print()    
        
# 본문
if __name__ == "__main__":
    q = CircularLinkedQueue() # 객체 생성
    MAX_QSIZE = 10 # 원형 연결 큐의 크기
 
    for i in range(8):
        q.enqueue(i) # 0, 1, ... , 7 대입
    
    q.display()
     
    for i in range(5):
        q.dequeue() # 전위부터 5개 반환하고 삭제
     
    q.display()
    
    for i in range(8,14):
        q.enqueue(i) # 8, 9, ... , 13 대입
     
    q.display()

'''
CircularLinkedQueue 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (fin) 
CircularLinkedQueue 5 -> 6 -> 7 (fin) 
CircularLinkedQueue 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 (fin) 
'''








