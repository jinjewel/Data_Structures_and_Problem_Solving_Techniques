#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.30
#######################################

# 최단경로 알고리즘이란
# 정점 U와 정점 V를 연결하는 경로 중에서 간선들의 가중치 합이 최소가 되는 경로
# 간선의 가중치는 비용, 거리, 시간 등이 있다.
# 알고리즘으로 Dijkstra와 Floyd 알고리즘이 있다.
# 간선이 없으면 가중치를 무한대로 처리
# -----------> 사진

# Dijkstra의 최단 경로 알고리즘(데이크스트라)
# 시작 정점 v에서 모든 다른 정점까지의 최단 경로 찾음
#   시작 정점 V : 최단 경로 탐색의 시작 정점
#   집합 S : 시작 정점 V로부터 최단경로가 이미 발견된 정점들의 집합
#   dist배열 : S에 있는 정점만을 거쳐서 다른 정점으로 가는 최단거리를 기록하는 배열
# 매 단계에서 최소 거리인 정점을 s에 추가
# 새로운 정점이 S에 추가되면 dist갱신 


# Dijkstra의 최단 경로 알고리즘
def choose_vertex(dist, selected):
    minv = 0 # 가중치의 최소 값을 가지는 인덱스를 저장할 변수
    mindist = INF # 가중치의 최소 값을 저장할 변수
    
    for v in range(len(dist)): # len(dist) = 정점의 수
        if selected[v] == False and dist[v] < mindist : # 가보지 않은 정점과 저장된 가중치보다 작은 가중치라면
            mindist = dist[v] # 가중치 저장
            minv = v # 인덱스 저장
    return minv # 인덱스 반환
    
def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx) # 정점 수
    dist = list(adj[start]) # start와 연결된 간선과 가중치 정보들을 리스트로 형변환하여 dist 저장
    path = [start] * vsize # 시작점을 정점의 수로 곱하여 다음을 뜻하는 Path 변수 생성
    found = [False] * vsize # 사이클을 막기위해 갔던 정점들을 표기하는 found 변수 생성
    found[start] = True # 시작점을 Ture 표시
    dist[start] = 0 # 시작점까지의 거리를 0으로 표시
    
    for i in range(vsize): # 정점의 수만큼 순환
        print("step%2d: "%(i+1), dist) # 단계별 dist[] 출력용, 현재 단계에서 각 목적지까지의 거리를 출력
        u = choose_vertex(dist, found) # 현재 거리와 지나간 정점정보 전달
        found[u] = True # 가중치가 가장 작은 U로 가야하기 때문에 U를 T로 표시
        
        for w in range(vsize): # 정점의 수만큼 순환
            if not found[w]: # 즉 가보지 않은 곳이라고 했다.
                if dist[u] + adj[u][w] < dist[w]: # U의 가중치 + U에서 W까지의 가중치 < 새로운 Q가지의 가중치
                    dist[w] = dist[u] + adj[u][w] # U를 걸쳐 두단계로 가는 것이 더 가중치가 작으면 갱신된다..
                    path[w] = u # 이전 정점 갱신
    return path # 찾아진 최단 경로 반환

if __name__ == "__main__":
    
    INF = 9999 # 최대값 상수로 지정
    
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # 이차원 배열에 인접 행렬을 표시
    weight = [[0, 7, INF, INF, 3, 10, INF],
              [7, 0, 4, 10, 2, 6, INF],
              [INF, 4, 0, 2, INF, INF, INF],
              [INF, 10, 2, 0, 11, 9, 4],
              [3, 2, INF, 11, 0, INF, 5],
              [10, 6, INF, 9, INF, 0, INF],
              [INF, INF, INF, 4, 5, INF, 0]] 
    
    print("Shortest Path By Dijkstra Algorithm")
    start = 0 # 시작점 설정
    path = shortest_path_dijkstra(vertex, weight, start) # 정점 그래프 시작점
    
    # 최종 경로를 출력하기 위한 코드
    for end in range(len(vertex)) : # 정점의 수만큼 순서대로 순환
        if end != start: # 도착점이 시작점이 아니면, 제자리끝점 로 가는게 아니면 거꾸로 출력함
            print("[최단경로: %s -> %s] %s"%(vertex[start], vertex[end], vertex[end]), end='')
            while (path[end] != start):
                print(" <- %s"%vertex[path[end]], end=' ')
                end = path[end]
            print(" <- %s"% vertex[path[end]])

# 출력
# Shortest Path By Dijkstra Algorithm
# step 1:  [0, 7, 9999, 9999, 3, 10, 9999]
# step 2:  [0, 5, 9999, 14, 3, 10, 8]
# step 3:  [0, 5, 9, 14, 3, 10, 8]
# step 4:  [0, 5, 9, 12, 3, 10, 8]
# step 5:  [0, 5, 9, 11, 3, 10, 8]
# step 6:  [0, 5, 9, 11, 3, 10, 8]
# step 7:  [0, 5, 9, 11, 3, 10, 8]
# [최단경로: A -> B] B <- E  <- A
# [최단경로: A -> C] C <- B  <- E  <- A
# [최단경로: A -> D] D <- C  <- B  <- E  <- A
# [최단경로: A -> E] E <- A
# [최단경로: A -> F] F <- A
# [최단경로: A -> G] G <- E  <- A







