#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.12
#######################################

# 큐(Queue) 와 스택(stack)은 파이썬에서 모듈을 제공
# 스택(stack) -> class lifoQueue
# 큐(Queue) -> class queue

# 파이썬 모듈로 큐 연산하기
import queue

Q = queue.Queue(maxsize=20) # queue클래스에 Queue함수, 인수로 크기 입력(최대 20)

for v in range(1, 10):
    Q.put(v) # enqueue가 put으로 재정의
    
print("큐의 내용: ", end="")

for _ in range (1,10):
    print(Q.get(), end=" ") # dequeue는 get으로 재정의
    
print()    
    
'''
큐의 내용: 1 2 3 4 5 6 7 8 9 
'''


