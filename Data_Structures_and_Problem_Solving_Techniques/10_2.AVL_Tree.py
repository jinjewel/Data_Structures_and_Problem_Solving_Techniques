#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.16
#######################################

## AVL 트리 : 균형이진탐색트리
# 모든 노드에서 왼쪽 서브트리와 오른쪽 서브트리의 높이 차가 1을 넘지 않은 이진탐색트리이다.
# 즉, 모든 노드의 균형 인수는 0이나 +1, -1이 되어야 한다.
# 최악,평균,최선 시간 복잡도 : O(log n)

# 탐색연산 : 이진탐색트리와 동일
# 삽입과 삭제 시 균형 상태가 깨질 수 있음, 따라서 삽입연산을 잘 시행해야함
# 균형이 깨지는 4가지 경우 : LL, LR, RR, RL 타입

from BinarySearchTree import *
from CircularQueue import CircularQueue

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
        return count_leaf(n.left) + count_leaf(n.right)
    
def count_height(n): # 트리의 높이를 구하는 함수
    if n is None: # 공백 트리 --> 0을 반환
        return 0
    hLeft = count_height(n.left) # 왼쪽 트리의 높이 계산
    hRight = count_height(n.right) # 오른쪽 트리의 높이 계산
    if (hLeft>hRight): # 더 높은 높이에 1을 더하여 반환
        return hLeft + 1
    else:
        return hRight + 1

def levelorder(root): # 레벨 순회 함수
    queue = CircularQueue() # 큐 객체 초기화
    queue.enqueue(root) # 최초에 큐에는 루트 노드만 들어있음.
    while not queue.isEmpty(): # 큐가 공백 상태가 아닌 동안 반복
        n = queue.dequeue() # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.key, end=' ') # 먼저 노드의 정보를 출력
            queue.enqueue(n.left) # n의 왼쪽 지식 노드를 큐에 삽입
            queue.enqueue(n.right) # n의 오른쪽 자식 노드를 큐에 삽입
            
# LL 회전 방법
def rotateLL(A):
    B = A.left # 시계방향으로 회전
    A.left = B.right
    B.right = A
    return A # 새로운 루트 A를 반환

# RR 회전 방법
def rotateRR(A):
    B = A.right # 반시계방향으로 회전
    A.right = B.left
    B.left = A
    return B # 새로운 루트 B를 반환

# RL 회전 방법
def rotateRL(A):
    B = A.right
    A.right = rotateLL(B) # LL회전
    return rotateRR(A) # RR회전

# LR 회전 방법
def rotateLR(A):
    B = A.left
    A.left = rotateRR(B) # RR회전
    return rotateLL(A) # LL회전

# 균형인수 계산
def calc_height_diff(A):
    if A is None: # 공백 트리 --> 0을 반환
        return 0
    hLeft = count_height(A.left) # 왼쪽 트리의 높이 계산
    hRight = count_height(A.right) # 오른쪽 트리의 높이 계산
    return hLeft - hRight

# 재균형인수 계산
def reBalance(parent): # 부모 노드의 균형 인수 계산, 왼쪽 - 오른쪽
    hDiff = calc_height_diff(parent)
    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)      
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)    
    return parent
    
def insert_avl(parent, node): # (부모노드, 자식노드)
    if node.key < parent.key: # 입력 노드의 키가 부모노드의 키보다 작을 때
        if parent.left != None: # 비어있지 않으면
            parent.left = insert_avl(parent.left, node) # 재귀호국, Parent.left = 재귀(parent.node)
        else:
            parent.left = node
        return reBalance(parent)
    elif node.key > parent.key: # 입력 노드의 키가 부모 노드의 키보다 클 때
        if parent.right != None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else: # 같을 때
        print("중복된 키 에러")
        
class AVLMap(BSTMap):
    def __init__(self):
        super().__init__()
        
    def insert(self, key, value = None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)
            
    def display(self, msg="AVLMap : "):
        print(msg, end=' ')
        levelorder(self.root)
        print()
    
if __name__ == "__main__":
    # node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    node = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    map = AVLMap()
    
    for i in node:
        map.insert(i)
        map.display("AVL(%d): "%i)
        
    print("노드의 개수 = %d"%count_node(map.root))
    print("단말의 개수 = %d"%count_leaf(map.root))    
    print("트리의 높이 = %d"%count_height(map.root))

'''
AVL(7):  7 
AVL(8):  7 8 
AVL(9):  8 7 9 
AVL(2):  8 7 9 2 
AVL(1):  8 7 9 
AVL(5):  8 7 9 5 
AVL(3):  8 7 9 
AVL(6):  8 7 9 6 
AVL(4):  8 7 9 
노드의 개수 = 3
단말의 개수 = 2
트리의 높이 = 2

AVL(0):  0 
AVL(1):  0 1 
AVL(2):  1 0 2 
AVL(3):  1 0 2 3 
AVL(4):  1 0 3 2 4 
AVL(5):  3 1 4 0 2 5 
AVL(6):  3 1 5 0 2 4 6 
AVL(7):  3 1 5 0 2 4 6 7 
AVL(8):  3 1 5 0 2 4 7 6 8 
AVL(9):  3 1 7 0 2 5 8 4 6 9 
노드의 개수 = 10
단말의 개수 = 5
트리의 높이 = 4
'''





