#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.26
#######################################

# 버블정렬

# 인접한 2개의 레코드를 비교하여 순서대로 교환
# 끝으로 이동한 레코도를 제외하고 다시 스캔 반복

# 복잡도 분석 : O(n^2) -> 최상, 평균, 최악의 경우 모두 일정

# 이동연산은 비교연산 보다 더 많은 시간이 소요됨

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False # 병렬의 중단을 나타내는 기준값
        for j in range(i): # step1은 i가 8이라 j가 0, ... , 7이다. step2은 i가 7이라 j가 0, ... , 6이다.
            if (A[j] > A[j+1]) : # 연속된 값들 중 초반에 있는 수가 더 크면
                A[j], A[j+1] = A[j+1], A[j] # 스왑
                bChanged = True # 기준값에 T값 저장
        if not bChanged: # False면 실행, 즉 한줄의 반복이 되는동안 스왑이 한번도 진행되지 않으면
            break;
        printStep(A, n-i);
        
def printStep(arr, val):
    print("   step %2d = " % (val), end='')
    print(arr)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("Original :  ", data)
    bubble_sort(data)
    print("Selection : ", data)   

# 출력
# Original :   [5, 3, 8, 4, 9, 1, 6, 2, 7]
#    step  1 = [3, 5, 4, 8, 1, 6, 2, 7, 9]
#    step  2 = [3, 4, 5, 1, 6, 2, 7, 8, 9]
#    step  3 = [3, 4, 1, 5, 2, 6, 7, 8, 9]
#    step  4 = [3, 1, 4, 2, 5, 6, 7, 8, 9]
#    step  5 = [1, 3, 2, 4, 5, 6, 7, 8, 9]
#    step  6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Selection :  [1, 2, 3, 4, 5, 6, 7, 8, 9]














