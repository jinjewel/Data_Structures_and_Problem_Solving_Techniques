#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.09
#######################################

# 큐는 선입선출(FIFO)의 자료구조이다.
# 후단(rear)에서 삽입을 하며 전단(front)에서 삭제를 하는 구조이다.

# 큐의 ADT(추상자료형)
# Queue() : 비어있으면 True를 아니면 False를 반환한다.
# isEmpty() : 큐가 비어있었으면 T를 아니면 F를 반환한다.
# enqueue(x) : 항목 x를 큐의 맨 뒤에 추가한다.
# dequeue() : 규의 맨 앞에 있는 항목을 꺼내 반환한다.
# peek() : 큐의 맨 앞에 있는 항목을 삭제하지 않고 반환한다.
# size() : 큐의 모든 항목들의 개수를 반환한다.
# clear(): 큐를 공백상태로 만든다.

# 큐의 응용
# 서비스 센터의 콜 큐
# 인쇄작업에 버퍼링 큐
# 실시간 비디오 스트리밍에서의 버퍼링 큐
# 공항과 은행등에서의 대기열

# 선형큐는 비효율적이다.
# 삽입연산 : O(1)
# 삭제연산 : O(n) -> 맨 앞에 항목을 꺼내서 반환해야 하므로

# 원형 큐 : 배열을 원형으로 사용. 실제 원형이 생긴 것이 아니라 선형 리스트를 원형 큐처럼 사용하는 것
# 선형 큐보단 월씬 효율적이다.

# 시계방향 회전 방법 : front = (front+1)%MAX_QSIZE or rear = (rear+1)%MAX_QSIZE
# 반시계방향 회전 방법 : front = (front-1+MAX_QSIZE)%MAX_QSIZE or rear = (rear-1+MAX_QSIZE)%MAX_QSIZE

# 공백상태 : front == rear
# 포화상태 : front % MAX_QSIZE == (rear+1) % MAX_QSIZE

# 파이썬 리스트를 사용하여 원형 큐 클래스 구현
class CircularQueue : 
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.MAX_QSIZE = 20 # 디폴트 값으로 20 , 전역으로 선언하면 알고리즘 상 좋지않다.
        self.items = [None]*self.MAX_QSIZE # 항목 저장용 리스트 [None, None, ...]
        
    def isEmpty( self ): # 공백상태
        return self.front == self.rear 
    
    def isFull( self ): # 포화상태
        return self.front == (self.rear + 1)%self.MAX_QSIZE
    
    def clear( self ): # 공백으로 만들기
        self.front = self.rear 

    def enqueue( self, item ): # 후미에 값 추가
        if not self.isFull():
            self.rear = (self.rear+1)%self.MAX_QSIZE
            self.items[self.rear] = item
            
    def dequeue( self ): # 전위에 값을 뽑고 삭제
        if not self.isEmpty():
            self.front = (self.front+1)%self.MAX_QSIZE
            return self.items[self.front] # 값이 자동으로 삭제된다. front가 변경될때 인덱스를 잃어버리며 링크가 잘리기 때문에
        
    def peek( self ): # 전위의 값을 복사하여 반환
        if not self.isEmpty():
            return self.items[(self.front + 1)%self.MAX_QSIZE]
        
    def size( self ): # 나머지의 성질을 이용하여 사이즈 계산
        return (self.rear - self.front + self.MAX_QSIZE) % self.MAX_QSIZE 
    
    def display( self ): # front, rear, queue 순서로 출력
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:self.MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%s, r=%s] ==> "%(self.front, self.rear), out)
        
# 본문

if __name__ == "__main__":    
    q = CircularQueue()
    q.MAX_QSIZE = 10 # 원형 큐의 크기 선언

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
[f=0, r=8] ==>  [0, 1, 2, 3, 4, 5, 6, 7]
[f=5, r=8] ==>  [5, 6, 7]
[f=5, r=4] ==>  [5, 6, 7, 8, 9, 10, 11, 12, 13]
'''