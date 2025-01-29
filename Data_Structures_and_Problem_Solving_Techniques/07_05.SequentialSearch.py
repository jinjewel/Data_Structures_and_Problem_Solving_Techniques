#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.26
#######################################

# 탐색, 맵, 엔트리, 딕셔너리

# 탐색 
# 테이블에서 원하는 탐색키를 가진 레코드를 찾는 작업

# 맵또는 딕셔너리
# 탐색을 위한 자료구조
# 엔트리 또는 키를 가진 레코드의 집합

# 맵 ADT
# search(key) : 탐색키(key)를 가진 레코드를 찾아 반환한다.
# insert(entry) : 주어진 entry를 앱에 삽입한다.
# delete(key) : 탐색키를 가진 레코드를 찾아 삭제한다.

# 엔트리 
# 키 : 영어 단어와 같은 레코드를 구분할 수 있는 탐색키
# 값 : 단어의 의미와 같이 같이 탐색키와 관련된 값

# 앱을 구현하는 방법
# 리스트 사용 : 정렬 / 비정렬
# 이진 탐색 트리 사용 (9장)
# 해싱 구조 이용


# 순차탐색

# 정렬되지 않은 배열에 적용 가능
# 가장 간단하고 직접적인 탐색 방법
# 시간 복잡도 : O(n)

# A에서 key값을 low인덱스부터 high인덱스까지 찾아서 반환한다.
def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            return i
    return None

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("Original :  ", data)
    idx = sequential_search(data, 1, 0, 9)
    print("sequential_search : ", idx+1) 
    
'''
출력
Original :   [5, 3, 8, 4, 9, 1, 6, 2, 7]
sequential_search :  6
'''    









