#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.05
#######################################

# 중위 표기 수식의 후위 표기 변환

# 중위와 루위 표기법의 공통점 : 피연산자의 순서가 동일
# 중위와 루위 표기법의 차이점 : 연산자의 순서만 다름(우선 순위 순서)

# 알고리즘
# 피연산자를 만나면 그래도 출력
# 연산자를 ㅁ나나면 스택에 저장했다가 스택보다 우선 순위가 낮은 연산자가 나오면 그때 출력
# 왼족 괄호는 우선수위가 가장낮은 연산자로 취금
# 오른족 괄호가 나오면 스택에서 왼쪽 괄호위에 쌓여있는 모든 연산자를 출력

from Stack_class import Stack
from evalPostfix import evalPostfix

def precedence (op): # 우선수위 판별 함수
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else :
        return -1

def Infix2Postfix( expr ): # expr : 입력 리스트(중위표기식)
    s = Stack() # s.top= [] 생성
    output = [] # output : 출력 리스트(후위 표기식)
    
    for term in expr :
        if term in '(': # 왼쪽 괄호이면
            s.push('(') # 스택에 삽입
        elif term in ')': # 오른쪽 괄호이면
            while not s.isEmpty(): # s.top= []가 채워져 있으면 반복
                op = s.pop() # 맨 위에 값 반환
                if op == '(': # 왼쪽 괄호가 나올때까지
                    break;
                else:
                    output.append(op) # 왼쪽 괄호를 만나면
        elif term in "+-*/": # 연산자이면
            while not s.isEmpty(): # s.top = []의 값들이 들어있으면 반복
                op = s.peek() # 스택에서 최근 값을 꺼내서
                if ( precedence(term) <= precedence(op)): # 현재 값과 우선순위 비교
                    output.append(op) # 현재 값의 우선순위가 최근 값의 우선순위보다 작거나 같으면
                    s.pop() # 후위표기 리스트에 추가
                else:
                    break
            s.push(term) # 현재 연산자 삽입
        else: # 피연산자 이면
            output.append(term) # 후위 표기 리스트에 추가
            
    while not s.isEmpty(): # s.top = []의 값이 있으면
        output.append(s.pop()) # 최근 값부터 차례대로 후위표기 리스트에 추가
        
    return output # 결과(후위 표기식 리스트)를 반환

# 본문
if __name__ == "__main__":
    infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')'] # 평범식1 (중위표기)
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')'] # 평범식2 (중위표기)
    postfix1 = Infix2Postfix(infix1) # 평범식1 -> 후위표기식1
    postfix2 = Infix2Postfix(infix2) # 평범식2 -> 후위표기식2
    result1 = evalPostfix(postfix1) # 후위표기식1의 값
    result2 = evalPostfix(postfix2) # 후위표기식2의 값

    # 출력
    print('중위표기: ', infix1)
    print('후위표기: ', postfix1)
    print('계산결과 : ', result1, end='\n\n')
    print('중위표기: ', infix2)
    print('후위표기: ', postfix2)
    print('계산결과 : ', result2)

'''
중위표기:  ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
후위표기:  ['8', '2', '/', '3', '-', '3', '2', '*', '+']
계산결과 :  7.0

중위표기:  ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
후위표기:  ['1', '2', '/', '4', '*', '1', '4', '/', '*']
계산결과 :  0.5
'''

