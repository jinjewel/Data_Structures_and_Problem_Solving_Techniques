#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.14
#######################################

# 변수의 범위
# 내장 범위 : 프로그램의 어디에서나 사용 할 수 있다.
# 전역 범위 : 프로그램 어디서나 사용 가능
# 지역 범위 : 함수나 클래스의 멤버함수(메소드) 안에서 생성
# 인스턴스 범위 : 클래스의 데이터 멤버로 생성된 변수

# 전역변수
# 예) 반지름

def calc_perimeter(radius) :
    # global perimeter
    print("파이 값: ", pi)
    perimeter = 2 * pi * radius
    return perimeter
    
pi = 3.14159
perimeter = 0
True_perimeter = calc_perimeter(10)
print("원둘레(r=10) = ", perimeter)    
print("원둘레(r=10) = ", True_perimeter)    

'''
파이 값:  3.14159
원둘레(r=10) =  0
원둘레(r=10) =  62.8318
'''