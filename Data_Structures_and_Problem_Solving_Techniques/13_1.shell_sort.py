#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 12.07
#######################################

## 다양한 정렬 알고리즘
# 간단한 정렬 알고리즘의 특징 O(N^2)
# 선택정렬 : 입력의 크기에 따라 자료 이동 횟수가 결정
# 삽입 정렬 : 레코드의 많은 이동이 필요, 대부분의 레코드가 이미 정렬되어 있는 경우에는 효율적
# 버블 정렬 : 가장 간단한 알고리즘

# 효율적인 알고리즘들
# 셸 정렬 : 삽입 정렬 개념을 개선한 방법
# 합 정렬 : 제자리 정렬로 구현하는 방법
# 병합 정렬 : 연속적인 분할과 병합을 이용
# 퀵 정렬, 이중피벗 퀵 정렬 : 피벗을 이용한 정렬
# 기수, 카운팅 정렬 : 분배를 이용해 정렬, 킷값에 제한이 있음

## 셸정렬

## 기본 아이디어
# 삽입 정렬은 어느 정도 정렬된 리스트에서 대단히 빠르지만 요소들이 이수한 위치로만 이동하므로 많은 이동 발생
# 요소들이 멀리 떨어진 위치로 이동할 수 있게 한다면 보다 적게 이동하여 제자리를 찾을 수 있음

## 알고리즘
# 리스트를 일정 간격의 부분 리스트로 나눔 - 나뉘어진 각각의 부분 리스트를 삽입 정렬 함
# 간격을 줄임 - 부분 리스트의 수는 더 작아지고, 각 부분 리스트는 더 커짐
# 간격이 1이 될 때까지 이 과정을 반복

## 장점 
# 불연속적인 부분 리스트에서 원거리 자료 이동으로 보다 적은 위치교환으로 제자리 찾을 가능성 증대
# 부분 리스트 점신적으로 정렬된 상태가 되므로 삽입 정렬 속도 증가

## 시간 복잡도
# 최악의 경우 : O(n^2)
# 평균적인 경우 : O(n^1.5)

def shell_sort(A):
    n = len(A)
    gap = n//2
    print('shell_')
    
    while gap>0:
        print('\nwhile 시작')
        print('원래 gap : ', gap)
        if (gap % 2) == 0 : 
            gap += 1
        print('정정한 gap : ', gap)
        for i in range(gap):
            
            print('\n   sortGapInsertion(A, %d, %d, %d)'%(i, n-1, gap), ' 함수 시작')
            sortGapInsertion(A, i, n-1, gap)
            print('   sortGapInsertion(A, %d, %d, %d)'%(i, n-1, gap), ' 함수 종료')
            
        print('\n   Gap=',gap,A)
        gap = gap//2
        
def sortGapInsertion(A, first, last, gap):
    
    print('      range(%d, %d, %d) for문 시작'%(first+gap, last+1, gap))
    for i in range(first+gap, last+1, gap):
        key = A[i]
        j = i - gap
        print('         key : ',A[i],' , j : ',j)
        while j >= first and key < A[j]:
            print('            whlie문 통과')
            A[j + gap] = A[j]
            j = j - gap
        print('         A[',j + gap,'] = ',key,' 으로 재정의')    
        A[j + gap] = key

if __name__ == "__main__":
    
    list = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print('data : ', list)
    print('\nshell 정렬 시작')
    
    shell_sort(list)
    print('\nshell : ', list)


'''
data :  [5, 3, 8, 4, 9, 1, 6, 2, 7]

shell 정렬 시작
shell_

while 시작
원래 gap :  4
정정한 gap :  5

   sortGapInsertion(A, 0, 8, 5)  함수 시작
      range(5, 9, 5) for문 시작
         key :  1  , j :  0
            whlie문 통과
         A[ 0 ] =  1  으로 재정의
   sortGapInsertion(A, 0, 8, 5)  함수 종료

   sortGapInsertion(A, 1, 8, 5)  함수 시작
      range(6, 9, 5) for문 시작
         key :  6  , j :  1
         A[ 6 ] =  6  으로 재정의
   sortGapInsertion(A, 1, 8, 5)  함수 종료

   sortGapInsertion(A, 2, 8, 5)  함수 시작
      range(7, 9, 5) for문 시작
         key :  2  , j :  2
            whlie문 통과
         A[ 2 ] =  2  으로 재정의
   sortGapInsertion(A, 2, 8, 5)  함수 종료

   sortGapInsertion(A, 3, 8, 5)  함수 시작
      range(8, 9, 5) for문 시작
         key :  7  , j :  3
         A[ 8 ] =  7  으로 재정의
   sortGapInsertion(A, 3, 8, 5)  함수 종료

   sortGapInsertion(A, 4, 8, 5)  함수 시작
      range(9, 9, 5) for문 시작
   sortGapInsertion(A, 4, 8, 5)  함수 종료

   Gap= 5 [1, 3, 2, 4, 9, 5, 6, 8, 7]

while 시작
원래 gap :  2
정정한 gap :  3

   sortGapInsertion(A, 0, 8, 3)  함수 시작
      range(3, 9, 3) for문 시작
         key :  4  , j :  0
         A[ 3 ] =  4  으로 재정의
         key :  6  , j :  3
         A[ 6 ] =  6  으로 재정의
   sortGapInsertion(A, 0, 8, 3)  함수 종료

   sortGapInsertion(A, 1, 8, 3)  함수 시작
      range(4, 9, 3) for문 시작
         key :  9  , j :  1
         A[ 4 ] =  9  으로 재정의
         key :  8  , j :  4
            whlie문 통과
         A[ 4 ] =  8  으로 재정의
   sortGapInsertion(A, 1, 8, 3)  함수 종료

   sortGapInsertion(A, 2, 8, 3)  함수 시작
      range(5, 9, 3) for문 시작
         key :  5  , j :  2
         A[ 5 ] =  5  으로 재정의
         key :  7  , j :  5
         A[ 8 ] =  7  으로 재정의
   sortGapInsertion(A, 2, 8, 3)  함수 종료

   Gap= 3 [1, 3, 2, 4, 8, 5, 6, 9, 7]

while 시작
원래 gap :  1
정정한 gap :  1

   sortGapInsertion(A, 0, 8, 1)  함수 시작
      range(1, 9, 1) for문 시작
         key :  3  , j :  0
         A[ 1 ] =  3  으로 재정의
         key :  2  , j :  1
            whlie문 통과
         A[ 1 ] =  2  으로 재정의
         key :  4  , j :  2
         A[ 3 ] =  4  으로 재정의
         key :  8  , j :  3
         A[ 4 ] =  8  으로 재정의
         key :  5  , j :  4
            whlie문 통과
         A[ 4 ] =  5  으로 재정의
         key :  6  , j :  5
            whlie문 통과
         A[ 5 ] =  6  으로 재정의
         key :  9  , j :  6
         A[ 7 ] =  9  으로 재정의
         key :  7  , j :  7
            whlie문 통과
            whlie문 통과
         A[ 6 ] =  7  으로 재정의
   sortGapInsertion(A, 0, 8, 1)  함수 종료

   Gap= 1 [1, 2, 3, 4, 5, 6, 7, 8, 9]

shell :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''




















