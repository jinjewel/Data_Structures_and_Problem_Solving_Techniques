#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.09
#######################################

## 힙 트리

## 힙
# '더미'와 모습이 비슷한 완전 이진트리 기반의 자료구조로 가장 크거나 작은 값을 빠르게 찾아내도록 만들어진 구조이다.
# '더미'란 : 
# 최대힙 : 부모 노드의 키값이 자식 노드의 키 값보다 크거나 같은 완전이진트리
# 최소힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전이진트리
# 즉, 완전 트리가 아니면 힙이 아님
# 완전 이진트리: 높이가 h일때 h-1까지는 꽉 차있고, h번째 레벨에는 순서대로 노드가 채워지는 경우
# 힙을 저장하는 효과적인 자료구조는 배열이다. 인덱스 0은 사용하지 않으며, 완전이진트리이므로 중간에 빈 칸이 없다.
# 우선순위 큐의 가장 좋은 구현 방법은 힙이다.
# 우선순위 큐 -> 힙 -> 배열

## 부모 노드와 자식 노드간의 인덱스 관계
# 노드 i의 부모 노드 인덱스는 i // 2 , 왼쪽 자식 인덱스는 i*2 , 오른쪽 자식 인덱스는 i*2+1 이다. 
# 노드의 개수가 n개면 간선의 개수는 n-1이다.
# 높이가 h이면 층의 노드는 0 ~ 2^(h-1)개의 노드를 가진다.
# 높이가 h이면 전체 노드는 h ~ 2^(h-1)개의 노드를 가진다.
# n개의 노드를 가진 이진 트리의 높이는 [log2(n+1)] ~ n 범위 안에 존재한다.

## Upheap : 추가가 되는 구조로 말단에서 위로 올라가는 구조
# 시간 복잡도 O(log n) : 루트 노드까지 올라가야 하므로 트리 높이에 해당하는 이동이 필요
## Downheap : 삭제가 되는 구조로 루트 노드가 삭제되며, 마지막 레벨의 마지막 노드를 루트노드로 올려서 노드를 내리는 구조
# 부모의 교환이 끝나면 마지막 층의 순서를 재배열 한다.
# 시간 복잡도 O(log n) : 가장 아래 레벨까지 내려가야 하므로 역시 트리의 높이 만큼의 시간이 걸린다.

class MaxHeap: # 최대힙 클래스
    def __init__(self): # 생성자
        self.heap = [] # 리스트(배열)를 이용한 힙
        self.heap.append(0) # 0번 항목은 사용하지 않음 -> 부모, 자식 간에 인덱스를 찾기 위해서
        
    def size(self): # 힙의 크기
        return len(self.heap) -1 # 0 인덱스는 사용하지 않으므로 -1이 필요
    
    def isEmpty(self): # 공백 검사
        return len(self.heap) == 0
    
    def Parent(self, i): # 부모 노드 값 반환
        return self.heap[i//2] # 정수의 나누기므로 // 사용
    
    def Left(self, i): # 왼쪽 자식 노드 값 반환
        return self.heap[i*2]
    
    def Right(self, i): # 오른쪽 자식 노드 값 반환
        return self.heap[i*2+1]
    
    def display(self, msg='힙트리: '): # 출력 형식 지정
        print(msg, self.heap[1:]) # 리스트의 슬라이싱 이용, 0번 인덱스는 사용하지 않으므로 [1:] 사용
        
    def insert(self, n): # up-heap
        self.heap.append(n) # 맨 마지막 노드로 일단 삽입
        i = self.size() # 노드 n의 위치, 맨뒤에 있으므로 총길이만큼의 인덱스가 부여
        while (i != 1 and n > self.Parent(i)): # 삽입된 노드가 맨 처음이 아니거나 부모노드 값보다 크면 반복
            self.heap[i] = self.Parent(i) # 자식이 부모보다 크므로 부모의 값을 자식에 대입
            i = i // 2 # 부모의 인덱스로 초기화, 자식의 값을 부모에 저장하기 위해, 현재 사용중인 인덱스(자식)를 부모 인덱스로 변환
        self.heap[i] = n # 부모 인덱스에 삽입하려는 값을 데입, 스위칭의 알고리즘이다.
        
    def delete(self): # down-heap
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1] # 쀼리노드 값을 저장
            last = self.heap[self.size()] # 마지막 노드 값을 저장
            while (child <= self.size()): # 마지막 인덱스까지 반복(child)
                # 인덱스를 벗어나지 않고 형제 노드간에 오른쪽 값이 더 크면
                # 무모노드와 비교하고 값을 바꾸기 위해 자식 노드 중에서 큰 값을 찾는 과정
                if child < self.size() and self.Left(parent) < self.Right(parent): 
                    child += 1
                if last >= self.heap[child]: # 마지막 노드값이 현재 기준 노드(child) 값보다 크면
                    break; # 삽입 위치를 찾음. down-heap 종료
                self.heap[parent] = self.heap[child] # 아니면 down-heap 계속 
                parent = child
                child *= 2;
                
            self.heap[parent] = last # last값이 parent에 해당하는 값보다 크면 삽입 자리를 찾은것이므로 last를 대입
            self.heap.pop(-1) # 맨 마지막 노드 삭제
            return hroot # 저장해두었던 투르를 반환


if __name__ == "__main__":
    heap = MaxHeap() # MaxHeap 객체 생성
    data = [2,5,4,8,9,3,7,3] # 힘에 삽입할 데이터
    print("[삽입 연산] : " + str(data)) 
    for elem in data: # 모든 데이터를 
        heap.insert(elem) # 힙에 삽입
    heap.display('[삽입 후]  : ') # 현재 힙 크리를 출력
    heap.delete() # 한번의 삭제 연산
    heap.display('[삭제 후]  : ') # 현재 힙 트리를 출력
    heap.delete() # 또 한번의 삭제 연산
    heap.display('[삭제 후]  : ') # 현재 힙 트리를 출력


'''
[삽입 연산] : [2, 5, 4, 8, 9, 3, 7, 3]

삽입과정 
2
5 2
5 2 4
8 5 4 2
9 8 4 2 5 
9 8 4 2 5 3
9 8 4 2 5 3 4
9 8 4 2 5 3 4 2

[삽입 후]  :  [9, 8, 7, 3, 5, 3, 4, 2]
[삭제 후]  :  [8, 5, 7, 3, 2, 3, 4]
[삭제 후]  :  [7, 5, 4, 3, 2, 3]
'''



















































