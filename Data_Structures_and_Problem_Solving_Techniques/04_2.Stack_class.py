#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.05
#######################################

# 스택의 구현
# 항목의 삽입/ 삭제 위치 : 파이썬 리스트의 후단을 사용하는 경우가 유리하다.

# 스택의 클래스 구현
class Stack:
    def __init__(self):
        self.top = []
        
    def isEmpty(self):
        return len(self.top) == 0   # 계산 결과가 True/False로 반환이 된다.

    def size(self):
        return len(self.top)  # 스택의 크기를 반환

    def clear(self):
        self.top = []

    def push(self, item):
        self.top.append(item)  # 리스트 맨뒤에 item을 추가한다.

    def pop(self):
        if not self.isEmpty(): # 공백상태가 아니면
            return self.top.pop(-1) # 리스트의 맨 뒤에서 항목을 하나 꺼내고 반환

    def peek(self):
        if not self.isEmpty():  # 공백상태가 아니면
            return self.top[-1]  # 맨 뒷 항목을 반환하고 삭제하지 않는다.
        
    def __str__(self): # 프린트가 되었을때 형식 지정, 이게 없을때는 <>가 있는 부분이 출력됨.
        return str(self.top[::-1]) # 순서를 역순으로 하여 stack의 성질로 출력하게 함

# 본문
if __name__ == "__main__":
    
    odd = Stack()
    even = Stack()
    
    for i in range(10):
        if i%2 == 0:
            even.push(i)
        else:
            odd.push(i)
            
    print(' 스택 even push 5회: ', even) # [0, 2, 4, 6, 8]
    print(' 스택 odd push 5회: ', odd) # [1, 3, 5, 7, 9]
    print(' 스택 even    peek: ', even.peek()) # 8
    print(' 스택 odd    peek: ', odd.peek()) # 9

    for _ in range(2):
        even.pop()
    for _ in range(3):
        odd.pop()       
    
    print(' 스택 even pop 2회: ', even) # [4, 2, 0] 
    print(' 스택 odd pop 3회: ', odd) # [3, 1] 
    
''' __str__설정을 하지 않고, even, odd로 출력하는 경우
 스택 even push 5회:  <__main__.Stack object at 0x000002AAC9811ED0> # 스택의 내용이 아니라 객체의 정보가 출력 
 스택 odd push 5회:  <__main__.Stack object at 0x000002AAC9811D50> # 스택의 내용이 아니라 객체의 정보가 출력 
 스택 even    peek:  8
 스택 odd    peek:  9
 스택 even pop 2회:  <__main__.Stack object at 0x000002AAC9811ED0> # 스택의 내용이 아니라 객체의 정보가 출력 
 스택 odd pop 3회:  <__main__.Stack object at 0x000002AAC9811D50> # 스택의 내용이 아니라 객체의 정보가 출력 
'''
''' __str__설정을 하지 않고, even.top, odd.top로 출력하는 경우
 스택 even push 5회:  [0, 2, 4, 6, 8]
 스택 odd push 5회:  [1, 3, 5, 7, 9]
 스택 even    peek:  8
 스택 odd    peek:  9
 스택 even pop 2회:  [0, 2, 4]
 스택 odd pop 3회:  [1, 3]
'''    
''' __str__설정을 하고, even, odd로 출력하는 경우
 스택 even push 5회:  [8, 6, 4, 2, 0]
 스택 odd push 5회:  [9, 7, 5, 3, 1]
 스택 even    peek:  8
 스택 odd    peek:  9
 스택 even pop 2회:  [4, 2, 0]
 스택 odd pop 3회:  [3, 1]
''' 





