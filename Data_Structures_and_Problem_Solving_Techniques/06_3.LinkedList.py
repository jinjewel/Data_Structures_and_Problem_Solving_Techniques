#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.19
#######################################

# 단순연결 리스트의 응용 : 연결된 리스트

# 연결된 리스트

# 노드 : 중간 다리 같은 역활을 하며 
# 데이터를 담을 데이터 필드와 링크를 담을 하나 이상의 필드가 필요하다.

# 연결 리스트 클래스

class Node: # 단순연결리스트를 위한 노드 클래스
    def __init__(self, elem, link=None): # 생성자, 디폴트 인수 사용
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = link # 링트 생성 및 초기화

class LinkedList: # 연결된 리스트 클래스
    def __init__(self):
        self.head = None
        
    def isEmpty(self): # 공백상태 검사
        return self.head == None
    
    def clear(self): # 리스트 초기화
        self.head = None
        
    def size(self): # 스택의 항목수 계산
        node = self.head # 시작노드를 새로운 공간(노드)에 저장한다.
        count = 0
        while not node == None: # node가 None이 아닐 때 까지
            node = node.link # 다음 노드로 이동
            count += 1 # count 증가
        return count # count 반환   
        
    def getNode(self, pos): # pos번째 노드 반환
        if pos < 0: # 입력된 pos값이 1보다 작을경우
            return None 
        node = self.head; # 시작노드를 새로운 공간(노드)에 저장한다.
        while pos > 0 and node != None: # pos가 0보다 크고 노드가 비어있지 않으면 반복
            node = node.link # node를 다음 노드로 이동
            pos -= 1 # 남은 반복 횟수 줄임
        return node # 최종 노드 반환

    def getEntry(self, pos): # pos번째 노드의 데이터 반환
        node = self.getNode(pos) # pos번째 있는 데이터를 찾아서 새로운 공간(노드)에 저장한다.
        if node == None: # 찾는 노드가 없는 경우
            return None 
        else: # 그 노드의 데이터를 반환
            return node.data

    def insert(self, pos, elem):
        before = self.getNode(pos-1) # 앞에 있는 노드를 찾아서 비포노드에 저장
        if before == None: # 비포노드에 값이 없으면, 시작노드 앞에 값을 대입.
            self.head = Node(elem, self.head) # 새롭게 만든 노드를 사작노드에 대입
        else: # 중간에 앞에 삽입하는 경우
            # 새로운 공간(노드)에 새로운 값과, 3번째 노드를 가리키던 before.link를 연결
            node = Node(elem, before.link)
            # 세번째 노드를 가리키던 before.link에 새로운 공간(노드)를 연결한다.
            before.link = node 

    def delete(self, pos):
        before = self.getNode(pos-1) # before 노드를 찾음
        if before == None: # 삭제하고 싶은 노드 앞에 노드가 없다면(시작노드를 삭제하는 경우)
            if self.head is not None : # 시작노드가 공백이 아니면(공백이면 안에 들어있는 값이 없다고 판단)
                 self.head = self.head.link # 시작노드를 시작노드에 연결된 노드로 연결
        elif before.link != None: # 중간에 있는 노드의사제 삭제
            before.link = before.link.link # 지우고 싶은 노드를 가리키는 링크(before.link)에 다음 노드를 연결한다.
            
    def display(self, msg='LinkedStack'): # 메세지를 출력(디폴트값을 미리 대입해 놓는다.)
        print(msg, end=" ") # 입력받은 값을 먼저 출력을 하고
        node = self.head # 헤드 포인트의 주소를 저장
        while not node == None: # 연결포인트에 값이 없지않으면 무한반복 
            print(node.data, end=" -> ") 
            node = node.link # 다음 연결포인트를 저장 
        print()
            
    def peek(self):
        if not self.isEmpty(): # 비어있지 않으면
            return self.head.data # 시작노드의 데이터를 반환      
            
    def replace(self, pos, elem): # 값을 대체
        node = self.getNode(pos) # 값을 대체할 노드의 위치를 찾는다.
        if node != None: # 그 노드가 존재한다면
            node.data = elem # 그 노드에 값에 새로 입력할 데이터를 삽입한다.

    def find(self, val): 
        count = 0
        node = self.head # 시작노드를 새로운 공간(노드)에 저장한다.
        while not node == None: # 노드에 더이상 값이 없을 경우까지 반복
            count += 1
            if node.data == val: # 만약 찾고있는 값이랑 같은경우
                break
            node = node.link
        return count    
        
# 본문
if __name__ == "__main__" :
        
    s = LinkedList()
    s.display('단순연결리스트로 구현한 리스트(초기상태):')
    
    s.insert(0,10)
    s.insert(0,20)
    s.insert(1,30)
    s.insert(s.size(), 40)
    s.insert(2,50)
    s.display('단순연결리스트로 구현한 리스트(삽입*5):')
    
    s.replace(2,90)
    s.display('단순연결리스트로 구현한 리스트(교체*1):')
    
    print('단순연결리스트로 구현한 리스트(값찾기): %d는 %d번째에 있다.'%(90, s.find(90)))

    s.delete(2);
    s.delete(s.size()-1)
    s.delete(0)
    s.display('단순연결리스트로 구현한 리스트(삭제*3):')
    
    s.clear()
    s.display('단순연결리스트로 구현한 리스트(정리후):')

'''
단순연결리스트로 구현한 리스트(초기상태): 
단순연결리스트로 구현한 리스트(삽입*5): 20 -> 30 -> 50 -> 10 -> 40 -> 
단순연결리스트로 구현한 리스트(교체*1): 20 -> 30 -> 90 -> 10 -> 40 -> 
단순연결리스트로 구현한 리스트(값찾기): 90는 3번째에 있다.
단순연결리스트로 구현한 리스트(삭제*3): 30 -> 10 -> 
단순연결리스트로 구현한 리스트(정리후): 
'''