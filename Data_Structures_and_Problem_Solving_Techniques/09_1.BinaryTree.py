#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.09
#######################################

## 트리란
# 계층적인 자료의 표현에 적합한 자료구조, 예) 회사 조직도, 컴퓨터의 폴더 구조
# 트리를 표현하는 방법은 많지만 이진트리만 다루도록 한다.

## 트리의 용어
# 루트 노드 : 뿌리 노드
# 간선 또는 에지 : 선
# 부모 / 자식 / 형제 / 조상 / 자손노드
# 단말 / 비단말 노드 : 최종 노드이면 단말 노드이다.
# 노드의 차수 : 생성되는 자식노드의 수
# 트리의 차수 : 뿌리노드의 차수 
# 레벨 : 트리의 층수를 말한다. 뿌리노드가 1레벨
# 트리의 높이 : 트리가 이루는 층의 개수를 말한다.
# 포레스트 : 트리들의 집합

## 이진트리 
# 모든 노드가 2개의 서브 트리를 갖는 트리로 서브 트리는 공집합일 수 있고, 순환적으로 정의된다.
# 노드의 개수가 n개면 간선의 개수는 n-1이다.
# 높이가 h이면 각 층의 노드의 수는 h ~ 2^(h-1)개의 노드를 가진다.
# 높이가 h이면 전체 노드의 수는 h ~ 2^h - 1개의 노드를 가진다.
# n개의 노드를 가진 이진 트리의 높이는 [log2(n+1)] ~ n 범위 안에 존재한다.
# 노드 i의 부모 노드 인덱스는 i // 2 , 왼쪽 자식 인덱스는 i*2 , 오른쪽 자식 인덱스는 i*2+1 이다. 

## 포화 이진트리
# 트리의 각 레벨에 노드가 꽉 차있는 이진트리
# 노드의 번호
#       1
#   2       3
# 4   5   6   7

## 완전 이진트리
# 높이가 h일때 h-1까지는 꽉 차있고, h번째 레벨에는 순서대로 노드가 채워지는 경우

## 이진트리의 연산
# 순회 : 트리에 속하는 모든 노드를 한 번씩 방문하는 것으로 선형 자료구조는 순회가 단순하다.
# 이진트리의 기본 순회는 전위, 중위, 후위(V가 기준)으로 나뉜다.
# 각 노드의 방문 순서
#              전위( VLR )                      중위( LVR )                      후위( LRV )
#               1                |               6                |               11                
#       2               7        |       4               8        |       5               10        
#   3       6       8       9    |   2       5       7       10   |   3       4       6       9   
# 4   5                   10  11 | 1   3                   9   11 | 1   2                   7   8   
# 가운데(V) -> 전반(L) -> 후반(R)   전반(L) -> 가운데(V) -> 후반(R)   전반(L) -> 후반(R) -> 가운데(V) 

from CircularQueue import CircularQueue

# 이진 트리의 노드 표현
class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data # 값이 들어갈 data
        self.left = left # 왼쪽 자식 노드로 연결하는 링크
        self.right = right # 오른쪽 자식 노드로 연결하는 링크
    
# 전위 순회 함수의 응용 예) 노드의 레벨 계산, 구조화된 문서 출력    
def preorder(n): # 전위 순회 함수, VLR
    if n is not None: # 비어있지 않다면
        print(n.data, end=' ') # 루트노드 처리, V
        preorder(n.left) # 왼쪽 서브트리 처리, L
        preorder(n.right) # 오른쪽 서브트리 처리, R
    
# 중위 순회 함수의 응용 예) 정렬
def inorder(n): # 중위 순회 함수, LVR
    if n is not None: # 비어있지 않다면
        inorder(n.left) # 왼쪽 서브트리 처리, L
        print(n.data, end=' ') # 루트노드 처리, V
        inorder(n.right) # 오른쪽 서브트리 처리, R
            
# 후위 순회 함수의 응용 예) 폴더 용량 계산
def postorder(n): # 후위 순회 함수, LRV
    if n is not None: # 비어있지 않다면
        postorder(n.left) # 왼쪽 서브트리 처리, L
        postorder(n.right) # 오른쪽 서브트리 처리, R
        print(n.data, end=' ') # 루트노드 처리, V
    
# 레벨 순회 함수 : (VRL) 전위 순회 알고리즘을 사용하여 큐를 이용하여 구현, 순환을 사용하지 않음
def levelorder(root): # 레벨 순회 함수
    queue = CircularQueue() # 큐 객체 초기화, 큐 -> (FIFO, LILO)
    queue.enqueue(root) # 최초에 큐에는 루트 노드만 들어있음. 루트노드를 처음으로 추가
    while not queue.isEmpty(): # 큐가 공백 상태가 아닌 동안 반복, 큐에 데이터가 없을 때까지 반복
        n = queue.dequeue() # 큐에서 맨 앞의 노드 n을 꺼냄, 큐에서 데이터를 꺼냄
        if n is not None: # 꺼낸 데이터가 비어있으면, 즉 최종노드이면 넘어감
            print(n.data, end=' ') # 먼저 노드의 정보를 출력, V
            queue.enqueue(n.left) # n의 왼쪽 지식 노드를 큐에 삽입, L
            queue.enqueue(n.right) # n의 오른쪽 자식 노드를 큐에 삽입, R
    
def count_node(n): # 순환을 이용해 트리의 노드 수를 계산하는 함수
    if n is None: # n이 None이면 공백 트리 --> 0을 반환
        return 0
    else: # 좌우 서브트리의 노드수의 합 +1을 반환 (순환이용)
        return 1 + count_node(n.left) + count_node(n.right)
        
def count_leaf(n): # 단말 노드(자식 노드가 없는 노드)의 수
    if n is None: # 공백 트리 --> 0을 반환
        return 0
    elif n.left is None and n.right is None: # 단말 노드이면 1을 반환
        return 1
    else: # 비단말 노드이면 좌우 서브트리의 결과값들을 합한다.
        return count_leaf(n.left) + count_leaf(n.right) # 순환을 사용한다.
        
def count_height(n): # 트리의 높이를 구하는 함수
    if n is None: # 공백 트리 --> 0을 반환
        return 0
    hLeft = count_height(n.left) # 왼쪽 트리의 높이 계산
    hRight = count_height(n.right) # 오른쪽 트리의 높이 계산
    if (hLeft>hRight): # 더 높은 높이에 1을 더하여 반환
        return hLeft + 1
    else:
        return hRight + 1

# 본문
if __name__ == "__main__":
    # 후위순회 순서대로 데이터를 입력
    d = TNode('D',None,None)
    e = TNode('E',None,None)
    b = TNode('B', d, e)
    f = TNode('F',None,None)
    c = TNode('C', f,None)
    root = TNode('A', b, c)
    
    print('\n    In-Order : ', end='')
    inorder(root) # 중위순회 LVR
    print('\n   Pre-Order : ', end='')
    preorder(root) # 전위순회 vLR
    print('\n  Post-Order : ', end='')
    postorder(root) # 추위 순회 LRV
    print('\n Level-Order : ', end='')
    levelorder(root) # 레벨 순회 
    print()
    
    print(" 노드의 개수 = %d개"%count_node(root))
    print(" 단말의 개수 = %d개"%count_leaf(root))    
    print(" 트리의 높이 = %d개"%count_height(root))    
    
'''
    In-Order : D B E A F C 
   Pre-Order : A B D E C F 
  Post-Order : D E B F C A 
 Level-Order : A B C D E F 
 노드의 개수 = 6개
 단말의 개수 = 3개
 트리의 높이 = 3개
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    