#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.26
#######################################

# 이진탐색

# 정렬된 배열의 탐색에 적합
# 배열의 중앙에 있는 값을 비교해가면서 탐색의 범위를 절반씩 줄여가는 탐색법

# 시간 복잡도 : O(log n)
# 반복으로 구현가능

def binary_search(A, key, low, high):
    if(low <= high): # 항목들이 남아있다면 (종료조건)
        middle = (low + high) // 2 # 중간값을 저장, 정수 나눗셈 //에 주의 할 것
        if key == A[middle]:
            return middle # 탐색 성공
        elif (key < A[middle]): # 찾는 값이 중간값보다 작으면 
            return binary_search(A, key, low, middle-1) # high 값을 수정하여 재귀
        else: # 찾는 값이 중간값보다 크면 
            return binary_search(A, key, middle+1, high) # low 값을 수정하여 재귀
    return None # 탐색 실패

if __name__ == "__main__":
    data = [2, 26, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]
    print("Original : ", data)
    idx = binary_search(data, 20, 0, len(data))
    print("binary_search : ", idx+1) 

'''
Original :  [2, 26, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]
binary_search :  6
'''

# 보간 탐색(InterPolation Search)
# 탐색키가 존재 할 위치를 예측하여 탐색
# 리스트를 불균등하게 분할하여 탐색

# 있다고만 하고 보간탐색 pass


