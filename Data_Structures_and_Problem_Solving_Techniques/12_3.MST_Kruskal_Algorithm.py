#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.30
#######################################

# 최소비용 신장트리(MST)
# 간선들의 가중치 합이 최소인 신장트리
# 반드시 (n-1)개의 간선만 사용, 사이클이 되면 안됨
# 사용 예) 도로, 통신, 배관 건설 : 모두 연결하면서 길이/비용을 최소화
# 사용 예) 전기 회로 : 단자를 모두 연결하면서 전선의 길이를 최소화

# MST의 알고리즘으로 2가지가 있다.
# 1. Kruskal 알고리즘 (크루스칼)
# 2. Prim 알고리즘 (프림)

# Kruskal MST(min 신장 tree) 알고리즘
# 탐욕적인 방법으로 그순간에 최적이라고 생각되는 것을 선택
# 각 단계에서 최선의 답을 선택하며 최종적인 해답에 도달
# 따라서 항상 최적의 해답을 주는지 검증이 필요하며, Kruskal MST 알고리즘은 증명이 됨

# Kruskal MST(최소 비용 신장 트리) 알고리즘
# 1. 그래프의 모든 간선을 가중치에 따라 오름차순으로 정렬한다.
# 2. 가장 가중치가 작은 간선 e를 뽑는다.
# 3. e를 신장트리에 놓었을때, 사이클이 생기면 넣지 않고 2번으로 이동
# 4. 사이클이 생기지 않으면 최소 신장 트리에 삽입한다.
# 5. n-1개의 간선이 삽입될 때까지 2번으로 이동

# 알고리즘
# -----------> 사진


parent = [] # 각노드의 부모노드 인덱스
set_size = 0 # 정점의 개수, 전역변수로 사용하기 위해 선언


def init_set(nSets): # 집합의 초기화 함수, nSets는 숫자로 받는다.
    global set_size, parent # 전역변수로 사용(변경)을 위함
    set_size = nSets; # 정덤의 개수를 전역변수에 저장
    for i in range(nSets): # 모든 정점에 대해  #  range(A, B) : A부터  B-1까지 반복, A가 없으면 0부터 B-1까지 반복
        parent.append(-1) # 각각이 고유의 집합(부모가 -1)
        
# 원소(대입값)가 속한 트리의(집합의) 뿌리 노드를(제일 위에 있는) 찾는 연산        
def find(id): # 정점 id가 속한 트리의 뿌리노드 찾기
    while (parent[id] >= 0): # id에 해당하는 부모노드가 -1이 아니면 반복, 
        # union에서 s1의 부모에 s2를 삽입하므로 parent는 그 인덱스 값을 가지는 노드에 부모노드를 나타낸다.
        id = parent[id] # id를 부모 id로 대입
    return id; # 최종 id 반환, 트리의 맨 위 노드의 id임

# S1, S2를 합치는 연산으로, S2의 뿌리노드를 S1의 부모노드로 하여 결합
def union(s1, s2): # s1, s2는 입력된 두 수가 각각 속하는 트리의 뿌리노드 값이다. 따라서 서로다른 트리를 합치는 과정
    global set_size # 전역변수 사용(변경)을 위함
    parent[s1] = s2 # s1을 s2의 뿌리노드에 연결, parent[s1] = s2
    set_size = set_size -1 # 정점을 연결했으므로 떨어져있는 정점의 개수 감소
    
def MSTKruskal(vertex, adj): # 매개변수 : 정점 리스트, 인접행렬
    vsize = len(vertex) # 정점의 개수
    init_set(vsize) # 정점의 개수와 부모 리스트 전역변수로 생성
    eList = [] # 간선 리스트
    
    # 모든 간선을 리스트에 넣음
    for i in range(vsize-1):
        for j in range(i+1, vsize): # 상 감각행렬의 모든 요소 출력
            if adj[i][j] != None: 
                eList.append( (i, j, adj[i][j]) ) # 간선 정보를 튜플로 변환하여 저장(숫자들로 이루어짐)
                
    # 간선 리스트를 가중치의 내림차순으로 정렬: 람다 함수 사용
    eList.sort(key=lambda e : e[2], reverse=True)
    
    adgeAccepted = 0 # 현재 이어진 간선 수를 저장
    while (adgeAccepted < vsize -1): # vsize(정점의 수)-1 = 간선의수
        e = eList.pop(-1) # 가장 작은 가중치를 가진 간선
        print('알고 싶은 부분 : ' , e, e[0], e[1], e[2], adj[e[0]])
        uset = find(e[0]) # e[0]가 속한 트리의 뿌리노드 값을 반환하는 과정
        vset = find(e[1]) # e[1]가 속한 트리의 뿌리노드 값을 반환하는 과정
        
        if uset != vset: # 두 뿌리노드값이 다르다면, 즉 서로 다른 트리라면
            print('간선 추가 : (%s, %s, %d)'%(vertex[e[0]], vertex[e[1]], e[2])) # 간선추가 출력
            union(uset, vset) # 두 집합을 합함, uset, vset 둘다 숫자이다.
            adgeAccepted += 1 # 간선이 하나 추가됨
            
if __name__ == "__main__":     
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # 이차원 배열에 인접 행렬을 표시
    weight = [[None, 29, None, None, None, 10, None],
              [29, None, 16, None, None, None, 15],
              [None, 16, None, 12, None, None, None],
              [None, None, 12, None, 22, None, 18],
              [None, None, None, 22, None, 27, 25],
              [10, None, None, None, 27, None, None],
              [None, 15, None, 18, 25, None, None]]   
    
    print("MST By Kruskal's Algorithm")
    MSTKruskal(vertex, weight)

'''
MST By Kruskal's Algorithm
알고 싶은 부분 :  (0, 5, 10) 0 5 10 [None, 29, None, None, None, 10, None]
간선 추가 : (A, F, 10)
알고 싶은 부분 :  (2, 3, 12) 2 3 12 [None, 16, None, 12, None, None, None]
간선 추가 : (C, D, 12)
알고 싶은 부분 :  (1, 6, 15) 1 6 15 [29, None, 16, None, None, None, 15]
간선 추가 : (B, G, 15)
알고 싶은 부분 :  (1, 2, 16) 1 2 16 [29, None, 16, None, None, None, 15]
간선 추가 : (B, C, 16)
알고 싶은 부분 :  (3, 6, 18) 3 6 18 [None, None, 12, None, 22, None, 18]
알고 싶은 부분 :  (3, 4, 22) 3 4 22 [None, None, 12, None, 22, None, 18]
간선 추가 : (D, E, 22)
알고 싶은 부분 :  (4, 6, 25) 4 6 25 [None, None, None, 22, None, 27, 25]
알고 싶은 부분 :  (4, 5, 27) 4 5 27 [None, None, None, 22, None, 27, 25]
간선 추가 : (E, F, 27)
'''
       