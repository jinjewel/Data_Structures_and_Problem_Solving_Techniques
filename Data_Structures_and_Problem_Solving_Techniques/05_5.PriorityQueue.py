#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.12
#######################################

# 우선순위 큐

# 응용분야
# 시뮬레이션, 네트워크 트래픽 제어, OS의 작업 스케쥴링 등

# 우선순의 큐의 ADT(추상자료형)
# PriorityQueue() : 비어있는 우선순위 큐를 만든다.
# isEmpty() : 우선순위 큐가 공백인지 검사한다.
# enqueue(e) :우선운위를 가진 항목 e를 추가한다.
# dequeue() : 가장 우선순위가 높은 항목을 꺼내서 반환한다.
# peek() : 가장 우선순위가 높은 요소를 삭제하지 않고 반환한다.
# size() : 우선순위 큐의 모든 항목들의 개수를 반환한다.
# clear() : 우선순위 큐를 공백 상태로 만든다.

# 일상의 흔한 데이터는 정렬이 되어있지 않다. 
# 그리고 그중에서 우선순위를 가지고 출력을 해야하는 경우도 있다. 그래서 이를 구현 해본다.
# 우선 순위를 판별하는 함수를 새롭게 만들어서 사용한다.

# 정렬되지 않은 배열을 가지고 우선순위 큐 생성 

# 정렬되지 않은 리스트 사용
# enqueue() : O(1)
# findMaxIndex() : O(n)
# dequeue() : O(n)
# peek() : O(n)

# 정렬된 리스크 사용
# enqueue() : O(n)
# dequeue() : O(1)
# peek() : O(1)

class PriorityQueue:
    def __init__( self ):
        self.items = [] # 항목을 저장하기 위한 리스트
        
    def isEmpty( self ):
        return len(self.items) == 0
    
    def size( self ):
        return len(self.items)

    def clear( self ):
        self.items = []
        
    def enqueue( self, item ): # 추가
        # 순서는 다시 정렬할 것이므로 그냥 대입한다. 큐를 리스트로 정의 했으므로 list.append(item)을 사용
        self.items.append( item ) 
        
    def dequeue( self ): # 우선순위가 가장 높은 항목을 출력 후 삭제
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)   
        
    def peek(self): # 우선순위가 가장 높은 항목을 출력
        highest = self.findMaxIndex()
        if highest is not None: # 값이 없지 않으면
            return self.items[highest] # List.pop(인덱스) : 인덱스 값 출력후 삭제
        
    def findMaxIndex( self ): # 우선순위 판단 함수
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range( 1, self.size()):
                if self.items[i] > self.items[highest]: # 가장큰 값을 가지는 인덱스 반환
                    highest = i
        return highest            
        
# 본문
if __name__ == "__main__":
    q = PriorityQueue() # 우선순위 큐 객체 생성, q.items = [] 생성
    q.enqueue(34) 
    q.enqueue(18)
    q.enqueue(27)    
    q.enqueue(45)
    q.enqueue(15) # 값 대입
    
    print("PQueue: ", q.items) # 정렬을 하지않은, 입력한 순서 그대로 출력
    
    while not q.isEmpty(): 
        print("Max Priority = ", q.dequeue(),", PQueue : ",q.items) # 배열 중 가장 큰 값을 반환

'''
PQueue:  [34, 18, 27, 45, 15]
Max Priority =  45 , PQueue :  [34, 18, 27, 15]
Max Priority =  34 , PQueue :  [18, 27, 15]
Max Priority =  27 , PQueue :  [18, 15]
Max Priority =  18 , PQueue :  [15]
Max Priority =  15 , PQueue :  []
'''

