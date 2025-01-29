#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.05
#######################################

# 회문인지 아닌지 확인하는 코드

# 함수 구현
from Stack_class import Stack

def palindrome(list):
    list = list.lower() # 대문자로 입력을 할 것을 대비하여 소문자로 
    list_re = [] # 콤마, 마침표, 괄호, 특수기호, 숫자 등의 문자를 제외한 문자열을 만들기 위해 공간 설정
    for s in list: # 콤마, 마침표, 괄호, 특수기호, 숫자 등이 입력 되는 것을 막기 위해 아스키코드 값을 사용
        if s >="a" and s <="z":
            strs.push(s) # 스택에 저장
            list_re.append(s) # 리스트에 저장
           
    num = 1 # 참일 경우 1을 유지 
    for i in range(strs.size()): # 자리수 만큼 비교를 한다.
        # 두 값이 리스트 형식이지만 리스트와 스택이므로 순서대로 비교하면 회문 비교가 가능
        if list_re[i] != strs.pop():  
            num = 0 # 거짓일 경우 0으로 변경
    return num # 참:1 / 거짓:0 을 반환        

def check_palindrome (num):
    if num == 1: 
        print("회문입니다.")        
    else:
        print("회문이 아닙니다.")    

# 본문

if __name__ == "__main__":
    
    strs = Stack() # 스택 생성
    list = input("회문인지 확인할 출력할 문자열을 입력하세요 :  ")
    num = palindrome(list) # 사용자 지정 함수를 이용하여 회문 검사
    check_palindrome(num) # 결과 출력        
      
'''
회문인지 확인할 출력할 문자열을 입력하세요 :  madam, i'm Adam
회문입니다.
'''
'''
회문인지 확인할 출력할 문자열을 입력하세요 :  madan, i'm Adam
회문이 아닙니다.
'''

      