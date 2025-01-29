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
# 1. Kruskal 알고리즘
# 2. Prim 알고리즘

# 2. Prim MST 알고리즘
# 하나의 정점에서부터 시작하여 트리를 단계적으로 확장
# 현재의 신장 트리 집합에 인접한 정점 중 최저 간선으로 연결된 정점을 선택하여 신장 트리 집합에 추가
# 이과정을 n-1개의 간선을 가질 때까지 반복

# Kruskal MST(최소 비용 신장 트리) 알고리즘
# 1. 그래프에서 시작 정점을 선택하여 초기 트리를 만든다. 
# 2. 현재 트리의 정점들과 인접한 정점들 중에서 간선의 가중치가 가장 작은 정점 v를 선택한다.
# 3. 이 정점 v와 이때의 간선을 트리에 추가한다.
# 4. 모든 정점이 삽입될 때 까지 2번으로 이동한다.

# 알고리즘
# A -> F -> E -> D(25보다 22가 작으므로) -> C(18보단 12가 작으므로) -> B -> G(29보단 15가 작으므로)

# Kruskal MST 알고리즘과 Prim MST 알고리즘비교
# Kruskal MST 알고리즘 : O(e log e)
# 대부분의 간선들을 정렬하는 시간에 좌우됨(가중치에 따라 역순으로 나열했으므로)
# 간선 e개를 정렬하는 시간, 간선이 적으면 유리
# 희박한 그래프가 유리

# 2. Prim MST 알고리즘 : O(n^2)
# 주 반복문이 n번, 내부 반복문이 n번 반복
# 밀집한 그래츠가 유리, 정점이 적으면 유리

def getMinVertex(dist, selected):
    minv = 0 # 가중치의 최소 값을 가지는 인덱스를 저장할 변수
    mindist = INF # # 가중치의 최소 값을 저장할 변수
    for v in range(len(dist)): # len(dist) = vsize로 정덤의 수이다.
        # 한번 들리지 않은 정점이고, 해당 dist 중 가장 작은 인덱스를 가장 가중치를 찾기 위한 값 비교
        if selected[v] == False and dist[v] < mindist : 
            mindist = dist[v] # 가중치 저장
            minv = v # 인덱스 저장
    return minv # 인덱스 반환
    
def MSTPrim(vertex, adj):
    vsize = len(vertex)# 정점의 수 저장
    # 정해진 시작점을 기준으로 정점이 이어져있엇다면, 그 정점에 해당하는 인덱스에 간선의 가중치 저장
    # 전에 사용된 내용을 리셋시키지 않고 사용,
    # != None으로 이어지지 않은 간선은 들르지 않았기 때문에 이어진 간선의 가중치만 재정의 함
    dist = [INF]*vsize # dist: [INF, INF, ... , INF]
    selected = [False]*vsize # selected: [False, ... , False]의 형태로 한 번 지나간 정점을 표시하는 리스트, 사이클 막는 변수
    dist[0] = 0 # dist: [0, INF, ... , INF] 첫번째를 0으로 삽입하여 A에서 출발하는 것을 표현
    
    for i in range(vsize): # 정점의 수만큼 반복, 0~5
        print()
        for x in range(vsize):
            print(dist[x],end=' ') 
        print()
            
        u = getMinVertex(dist, selected) # 가장 작은 인덱스 반환
        selected[u] = True # 다시 뒤로 가지 않게 F -> T로 설정, 한번 지나간 점을 T로 표현하여 사이클을 막는다.
        print(vertex[u], end=' ') # getMinVertex로 찾은 가중치가 작은 정점을 지나기 위해 출력
        for v in range(vsize): # 간선의 수만큼 반복
            if (adj[u][v] != None): # 출발점 u를 기준으로 이어진 간선이 있다면
                # V를 목표지점이라고 할 때, V정점을 들르지 않고, 현재 dist에 저장되어있는 가중치보다 현재 dist에 자장되어있는 
                if selected[v] == False and adj[u][v] < dist[v]: # 가중치보다 현재 (U,V)간선 가중치가 작으면
                    dist[v] = adj[u][v] # 가중치 재정의
    print()

if __name__ == "__main__":
    INF = 9999
    
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # 이차원 배열에 인접 행렬을 표시
    weight = [[None, 29, None, None, None, 10, None],
              [29, None, 16, None, None, None, 15],
              [None, 16, None, 12, None, None, None],
              [None, None, 12, None, 22, None, 18],
              [None, None, None, 22, None, 27, 25],
              [10, None, None, None, 27, None, None],
              [None, 15, None, 18, 25, None, None]]
    
    print("MST By Prim's Algorithm")
    MSTPrim(vertex, weight)

'''
MST By Prim's Algorithm

0 9999 9999 9999 9999 9999 9999 
A 
0 29 9999 9999 9999 10 9999 
F 
0 29 9999 9999 27 10 9999 
E 
0 29 9999 22 27 10 25 
D 
0 29 12 22 27 10 18 
C 
0 16 12 22 27 10 18 
B 
0 16 12 22 27 10 15 
G 
'''









