#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.14
#######################################

# 파이썬 내장 함수 : type(), len(), ord() 등
# 사용자 정의함수

# 여러개의 값의 반환
# 예) 최소, 최대 값 찾는 함수
def find_min_max(A):
    min = A[0]
    max = A[0]
    for i in range(1, len(A)):
        if max < A[i] : max = A[i]
        if min > A[i] : min = A[i]
    return min, max

# 디폴트 인수
# 예) 더하는 함수
def sum_range(begin, end, step=1): # 매개변수 step이 기본값을 가짐
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum



if __name__ == "__main__":
    
    # 여러개의 값의 반환
    # 예) 최소, 최대 값 찾는 함수
    data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7]
    x, y = find_min_max(data)
    print("(min, max) = ", (x, y))

    '''
    (min, max) =  (1, 9)
    '''

    # 디폴트 인수
    # 예) 더하는 함수
    print("sum = ", sum_range(1, 10)) # step은 디폴트 값(1)으로 처리됨)
    print("sum = ", sum_range(1, 10, 2))

    '''
    sum =  45
    sum =  25
    '''

    # 키워드 인수
    print("sum = ", sum_range(step=3, begin=1 , end=10))
    print("game ", end=" " ) # 라인피드가 발생하지 않음(키워드 인수 사용)

    '''
    sum =  12
    game  
    '''