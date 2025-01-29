#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.19
#######################################

# 회문을 검사라는 함수(연결된스택 사용)

from LinkedStack import LinkedStack
from LinkedStack import Node

def Palindrome(list):
    list1 = list
    list = list.lower() # 대문자로 입력을 할 것을 대비하여 소문자로 변경
    list2 = [] # 콤마, 마침표, 괄호, 특수기호, 숫자 등을 제거한 리스트를 저장하기 위해 공간 생성
    
    for s in list: # 콤마, 마침표, 괄호, 특수기호, 숫자 등이 입력 되는 것을 막기 위해 아스키코드 값을 사용
        if s >="a" and s <="z":
            strs.push(s) # 연결스택에 값을 대입한다. 
            list2.append(s) # 리스트에 값을 대입한다.
 
    print("입력된 문자열 : ", ''.join(list1))
    print("정제된 문자열 : ",''.join(list2))
    
    num = 1 # 참일 경우 1을 유지 
    for i in range(strs.size()): 
        if list2[i] != strs.pop(): # 양쪽에 값을 비교하고 삭제하며 회문을 검사
            num = 0 # 거짓일 경우 0으로 변경
    return num # 참:1 / 거짓:0 을 반환 

# 본문
if __name__ == "__main__":
    strs = LinkedStack() 
    list = input("회문인지 확인할 출력할 문자열을 입력하세요 : ")
    num = Palindrome(list) # 사용자 지정 함수를 이용하여 회문 검사
    print("회문입니다.") if num==1 else print("회문이 아닙니다.") # 출력문 작성

'''
회문인지 확인할 출력할 문자열을 입력하세요 : madam, i'm Adam
입력된 문자열 :  madam, i'm Adam
정제된 문자열 :  madamimadam
회문입니다.
'''
'''
회문인지 확인할 출력할 문자열을 입력하세요 : a"sDf..gF-d,Ea
입력된 문자열 :  a"sDf..gF-d,Ea
정제된 문자열 :  asdfgfdea
회문이 아닙니다.
'''
        
        