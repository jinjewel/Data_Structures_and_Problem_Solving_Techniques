#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 12.07
#######################################

## 퀵 정렬 -- 코드는 넘어간다.
# 분할 정복법 사용
# 리스트를 2개의 부분 리스트로 비 균등 분할
# 각각의 부분리스트를 다시 퀵 정렬함(순환 호출)

## 복잡도 분석
# 최선의 경우
# 균등 분할
# 패스 수 : log n
# 복잡도 : O(n log n)

# 최악의 경우
# 이미 정렬된 리스트
# 패스 수 : n
# 복잡도 : O(n^2)

def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q-1)
        quick_sort(A, q+1, right)

def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high):
        while low <= right and A[low] < pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1
            
        if low < high:
            A[low], A[high] = A[high], A[low]
            
    A[left], A[high] = A[high], A[left]
    return high

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print('     data : ', data)    
    quick_sort(data, 0, len(data)-1)
    print('QuickSort : ', data)

'''
     data :  [5, 3, 8, 4, 9, 1, 6, 2, 7]
QuickSort :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
