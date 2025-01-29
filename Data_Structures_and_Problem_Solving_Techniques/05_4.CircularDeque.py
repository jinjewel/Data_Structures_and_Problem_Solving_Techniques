#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.12
#######################################

# 덱은 스택이나 큐보다는 입출력이 자유로운 자료구조이다.

# 덱(deque : double ended queue) : 전단과 후단에서 모두 삽입과 출력이 가능

# 덱의 ADT(추상자료형)
# Deque() : 비어 있는 새로운 덱을 만든다.
# isEmpty() : 덱이 비어있으면 T, 아니면 F를 반환한다.
# addFront(x) : 항목 x를 덱의 맨 앞에 추가한다.
# deleteFront() : 맨 앞의 항목을 꺼내서 반환한다.
# getFront : 맨 앞의 항목을 꺼내지 않고 반환한다.
# addRear(x) : 항목 x를 덱의 맨 뒤에 추가한다.
# deleteRear() : 맨 뒤의 항목을 꺼내서 반환한다.
# getRear() : 맨 뒤의 항목을 꺼내지 않고 반환한다.
# isFull() : 덱이 가득 차 있으면 T, 아니면 F를 반환한다.
# size() : 덱의 모든 항목들의 개수를 반환한다.
# clear() : 덱을 공백 상태로 만든다.

# 덱의 연산 : 스택과 큐의 연산과 같다.
#            add         delete        get 
# Front   push(스택)   dequeue(큐)    peek(큐)
# Rear   enqueue(큐)   pop(츠택)     peek(스택)

# 시계방향 회전 방법 : front = (front+1)%MAX_QSIZE or rear = (rear+1)%MAX_QSIZE
# 반시계방향 회전 방법 : front = (front-1+MAX_QSIZE)%MAX_QSIZE or rear = (rear-1+MAX_QSIZE)%MAX_QSIZE

# 원형 덱 구현
from CircularQuenue import CircularQueue

class CircularDepue(CircularQueue): # CircularQueue에서 상속
    
    def __init__( self ):
        super().__init__() # 부모 클래스에서 생성자 호출
        
    # 전위 계산
    def addFront( self, item): # 값 추가
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front - 1 + self.MAX_QSIZE) % self.MAX_QSIZE # 반시계 방향으로 회전
    
    def deleteFront( self ):
        return self.dequeue() # 부모 클래스(큐)에서 함수 호출, 시계 방향으로 회전
    
    def getFront( self ):
        return self.peek() # 부모 클래스(큐)에서 함수 호출            

    # 후위 계산    
        
    def addRear( self, item ):
        self.enqueue( item ) # 부모 클래스(큐)에서 함수 호출, 시계 방향으로 회전
                   
    def deleteRear( self ): # 값을 리턴하고 삭제
        if not self.isEmpty():
            item = self.items[self.rear]; # 인덱스를 바꾸면서 값을 삭제
            self.rear = (self.rear - 1 + self.MAX_QSIZE) % self.MAX_QSIZE # 반시계 방향으로 회전
            return item
        
    def getRear( self ): # 값만 리턴
        return self.items[self.rear]
    
# 본문
if __name__ == "__main__":
    
    dq = CircularDepue() # 덱 선언
    dq.MAX_QSIZE = 10
    
    for i in range(9):
        if i%2 == 0: # 짝수는 뒤에서 입력
            dq.addRear(i)
        else: # 홀수는 앞에서 입력
            dq.addFront(i)
    
    dq.display()
    
    for i in range(2): # 전단에서 삭제
        dq.deleteFront()
        
    for i in range(3): # 후단에서 삭제
        dq.deleteRear()
          
    dq.display()    

    for i in range(9,14):
        dq.addFront(i)
        
    dq.display()    
'''
[f=6, r=5] ==>  [7, 5, 3, 1, 0, 2, 4, 6, 8]
[f=8, r=2] ==>  [3, 1, 0, 2]
[f=3, r=2] ==>  [13, 12, 11, 10, 9, 3, 1, 0, 2]
'''

