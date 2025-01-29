#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.05
#######################################

# 역순 출력

from Stack_class import Stack

stack = Stack() # 스택을 위한 stack.top =[] 리스트 생성
strs = input("역순으로 출력할 문자열을 입력하세요 :  ")

for s in strs: 
    stack.push(s) # 역순으로 입력
    
# 스택(리스트)으로 출력    
print(stack) # 스틱을 리스트 형식으로 만들었지 때문에 리스트 형식으로 출력된다.
# 스택(리스트)을 문자열로 변환하여 출력
print(''.join(stack.pop() for _ in range(len(strs))))

'''
역순으로 출력할 문자열을 입력하세요 :  list
['t', 's', 'i', 'l']
tsil
'''