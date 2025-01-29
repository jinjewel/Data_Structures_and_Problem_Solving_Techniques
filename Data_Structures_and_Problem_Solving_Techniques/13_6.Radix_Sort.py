#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 12.07
#######################################

## 기수정렬
# 레코드를 비교하지 않고 분배하여 정렬 수행
# 비교에 의한 정렬의 하한인 O(n log n)보다 좋을 수 있음
# 시간복잡도 : O(dn), 대부분 d<10 이하

## 아이디어
# 단순히 자리수에 따라 숫자를 bucket에 넣었다가 꺼내면 정렬됨
# 두자리수 이상 기수는 낮은 자릿수 분류하고 순서대로 읽으면서 높은 자리수를 분류를 진행하면 된다.

## 버킷(큐)의 개수는 키의 표현 방법과 밀접한 관꼐
# 이진법을 사용한다면 버킷은 2개
# 알파벳 문자를 사용한다면 버킷은 26개
# 십진법을 사용한다면 버킷은 10개

## n개의 레코드 d개의 자릿수 키의 기수 정렬
# 메인 루프는 자릿수 d번 반복
# 큐에 n개 레코드 입력 수행

## 단점
# 정렬할 수 있는 레코드의 타입 한정
# 정수나 단순 문자(알파벳 등)이어야만 함
# 실수, 한글, 한자로 이루어진 키는 정렬 못함

import random
from queue import Queue

def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())
        
    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[ ( A[i]//factor )%10 ].put(A[i])
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                i += 1
        
        factor *= 10
        print("step", d+1, A)

if __name__ == "__main__":
    
    BUCKETS = 10 # data 수
    DIGITS = 4 # 각 숫자의 자리수
    data = []
    for i in range(10):
        data.append(random.randint(1,9999))
    print(" data :", data)
    print("\nRadixSort Start")
        
    radix_sort(data)
    print("\nRadixSort:", data)

'''
 data : [4279, 663, 2976, 9632, 92, 5073, 500, 4141, 8017, 6680]

RadixSort Start
step 1 [500, 6680, 4141, 9632, 92, 663, 5073, 2976, 8017, 4279]
step 2 [500, 8017, 9632, 4141, 663, 5073, 2976, 4279, 6680, 92]
step 3 [8017, 5073, 92, 4141, 4279, 500, 9632, 663, 6680, 2976]
step 4 [92, 500, 663, 2976, 4141, 4279, 5073, 6680, 8017, 9632]

RadixSort: [92, 500, 663, 2976, 4141, 4279, 5073, 6680, 8017, 9632]
'''








