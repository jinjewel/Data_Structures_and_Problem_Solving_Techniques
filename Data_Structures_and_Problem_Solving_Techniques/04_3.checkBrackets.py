#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.05
#######################################

# 스택의 용도 : 괄호검사

# 괄호 검사란

# # 괄호검사 알고리즘
# 조건 1 : 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
# 조건 2 : 같은 타입의 괄호에서 외쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다.
# 조건 3 : 서로 다른 타입의 괄호 쌍이 서로를 교차하면 안된다.

from Stack_class import Stack

def checkBrackets(statement): # 한 문장에서 검사 함수
    stack = Stack()
    
    for ch in statement:
        if ch in ('{', '[', '('): # 왼쪽 괄호이면
            stack.push(ch) # 대입
        elif ch in ('}', ']', ')'): # 오른족 괄호이면
            if stack.isEmpty(): # 왼쪽 괄호가 이미 저장되어있나 확인. 
                return False # 없으면 조건 2 위반
            else: # 값(왼쪽 괄호)이 있으면
                left = stack.pop() # 꺼내와서
                if (ch == "}" and left != "{") or (ch == "]" and left != "[")  or (ch == ")" and left != "("):
                    return False # 괄호의 짝이 맞지 않으면 조건 3 위반
    return stack.isEmpty() # False이면, 즉 오른쪽 부분이 없는데 왼쪽부분이 스택에 남아 있다면 조건 1 위반       
                    
def checkBracketsVer2(lines): # 여러 문장에서 검사 함수
    stack = Stack()
    
    for line in lines: # 전체 라인을 불러오고
        for ch in line: # 각 라인을 따로 불러서 확인한다.
            if ch in ('{', '[', '('): # 왼쪽 괄호이면
                stack.push(ch) # 대입
            elif ch in ('}', ']', ')'): # 오른족 괄호이면 
                if stack.isEmpty(): # 왼쪽 괄호가 이미 저장되어있나 확인. 
                    return False # 없으면 조건 2 위반
                else: # 값(왼쪽 괄호)이 있으면
                    left = stack.pop() # 꺼내와서
                    if (ch == "}" and left != "{") or (ch == "]" and left != "[")  or (ch == ")" and left != "("):
                           return False # 괄호의 짝이 맞지 않으면 조건 3 위반
    return stack.isEmpty() # False이면, 즉 오른쪽 부분이 없는데 왼쪽부분이 스택에 남아 있다면 조건 1 위반  

# 본문
if __name__ == "__main__":
    
    str = ( "{ A[(i+1)] = 0; }", "if( (i==0) && (j==0)", "A[ (i+1] ) = 0;" )
    for s in str:
        m = checkBrackets(s)
        print(s, "---> ", m) 

    # filename = "Stack_class.py"
    filename = "test.txt" # 괄호가 부족함. // test.txt -> [{( )]
    infile = open(filename, "r", encoding='UTF8')
    lines = infile.readlines();
    infile.close()
    
    result = checkBracketsVer2(lines)
    print("\n", filename, " ---> ", result) # test.txt  --->  False

'''
{ A[(i+1)] = 0; } --->  True
if( (i==0) && (j==0) --->  False
A[ (i+1] ) = 0; --->  False

 test.txt  --->  False
'''














