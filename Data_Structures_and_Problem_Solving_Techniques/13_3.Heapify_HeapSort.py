#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 12.07
#######################################

## 제자리 정렬로 구현한 힙 정렬

## 알고리즘
# 1단계 : 리스트를 최대힙으로 만듦
# 2단계 : 최대힙을 정렬된 리스트로 만듦
# Heapify : 최대힙을 만드는 과정

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l<n and arr[i] < arr[l]:
        largest = l
    if r<n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
            
def heapSort(arr):
    n = len(arr)
    print("i=",0, arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
        print("i=",i, arr)
    print()
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print("i= ",i, arr)

if __name__ == "__main__":
    dataL = [5, 3, 8, 4, 9, 1, 6, 2, 7] 
    
    heapSort(dataL)
    
    print('HeapSort : ',dataL)




