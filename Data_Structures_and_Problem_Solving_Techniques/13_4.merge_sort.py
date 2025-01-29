#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 12.07
#######################################

## 병합 정렬

## 분할 정복 방법
# 문제를 보다 작은 2개의 문제로 분리하고 각 문제를 해결한 다음, 결과를 모아서 원래의 문제를 해결하려는 전략

## 시간 복잡도
## 비교횟수
# 크기 n인 리스트를 균등 분배하므로 log(n)개의 패스
# 각 패스에서 레코드 n개를 비교, n번 비교 연산
## 이동횟수
# 각 패스에서 2n의 이동 발생 -> 전체 이동 2n * log(n)
## 시간복잡도
# O(n log n)

## 분석
# 효율적인 알고리즘
# 최적, 평균, 최악의 경우에도 동일한 시간에 정렬
# 추가적인 메모리가 필요

def merge_sort(A, left, right):
    if left < right:
        mid = (left+right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)
        
def merge(A, left, mid, right):
    global sorted
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k= i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1
            
    if i > mid:
        sorted[k : k+right-j+1] = A[j:right+1]
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]
    A[left:right+1] = sorted[left:right+1]
    
    
if __name__ == "__main__":
    sorted = []
    data = [10,12,20,27,13,15,22,25]
    sorted = [0]*len(data)
    print('     data : ', data)
    merge_sort(data, 0, len(data)-1)
    print('MergeSort : ', data)

'''
     data :  [10, 12, 20, 27, 13, 15, 22, 25]
MergeSort :  [10, 12, 13, 15, 20, 22, 25, 27]
'''


