#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.12
#######################################

# 덱을 사용하여 회문인지 아닌지 확인하는 코드

# 함수 구현
from CircularQuenue import CircularQueue
from CircularDeque import CircularDepue

def palindrome(list):
    list = list.lower() # 대문자로 입력을 할 것을 대비하여 소문자로 변경
    # strs.MAX_QSIZE = len(list) + 1, 왜 안되는 것인가? input 문장 : madam, i'm Adam 
    # 현재는 CircularQueue의 MAX_QSIZE값을 10 -> 20으로 하여 (11)자의 문장을 비교할 수 있다.
    for s in list: # 콤마, 마침표, 괄호, 특수기호, 숫자 등이 입력 되는 것을 막기 위해 아스키코드 값을 사용
        if s >="a" and s <="z":
            strs.addRear(s) # 후미대입 : 후미에 값을 계속 대입한다. 
           
    num = 1 # 참일 경우 1을 유지 
    strs.display()
    for i in range(strs.size() // 2): # 자리수를 2로 나눈 몫만큼 반복한다. 양쪽에서 비교하고 삭제하므로
        if strs.deleteFront() != strs.deleteRear(): # 양쪽에 값을 비교하고 삭제하며 회문을 검사
            num = 0 # 거짓일 경우 0으로 변경
    return num # 참:1 / 거짓:0 을 반환        

def check_palindrome(num):
    if num == 1: 
        print("회문입니다.")        
    else:
        print("회문이 아닙니다.")

# 본문
if __name__ == "__main__":
    strs = CircularDepue() # 덱 객체 생성
    list = input("회문인지 확인할 출력할 문자열을 입력하세요 :  ")
    num = palindrome(list) # 사용자 지정 함수를 이용하여 회문 검사         
    check_palindrome(num) # 결과 출력        
              
'''
회문인지 확인할 출력할 문자열을 입력하세요 :  asDFg, f;. dS..  A
[f=0, r=9] ==>  ['a', 's', 'd', 'f', 'g', 'f', 'd', 's', 'a']
회문입니다.

회문인지 확인할 출력할 문자열을 입력하세요 :  madam, i'm Adam
[f=0, r=11] ==>  ['m', 'a', 'd', 'a', 'm', 'i', 'm', 'a', 'd', 'a', 'm']
회문입니다.

회문인지 확인할 출력할 문자열을 입력하세요 :  asD, 'gS.a
[f=0, r=6] ==>  ['a', 's', 'd', 'g', 's', 'a']
회문이 아닙니다.
'''


