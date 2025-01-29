#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.23
#######################################

## 신장 트리란
# 인접 리스트로 구현을 하며 그래프 내의 모든 정점을 포함하는 트리이다.
# 인접한 두 정점을 이어주는 간선을 순서대로 출력하는 코드이다.
# 사이클을 포함하면 안됨, 간선의 수 = n -1 

## DFS : 깊이 우선 탐색(depth - first search)
# 스택 사용

## BFS : 너비 우선 탐색(breadth-first search)
# 큐 사용

import collections

# 너비 우선 탐색을 기준으로 한 신장트리
def bfsST(graph, start):
    visited = set([start]) # 맨 처음에는 start만 방문한 정점임
    queue = collections.deque([start]) # 파이썬 컬렉션의 덱 생성(큐로 사용)
    while queue: # 공백이 아닐때까지
        v = queue.popleft() # 큐에서 하나의 정점 v를 빼냄
        nbr = graph[v] - visited # nbr = {v의 인접벙점} - {방문정점}
        for u in nbr: # 갈 수 있는 모든 인접 정점에 대해
            print("(", v, ",", u, ")", end= "") # (v, n) 간선 추가
            visited.add(u) # 이제 u는 방문 했음
            queue.append(u) # u를 큐에 삽입

if __name__ == "__main__":
    
    mygraph = { "A" : set(["B", "C"]),
               "B" : set(["A"]),
               "C" : set(["A"]),
               "D" : set(["E"]),
               "E" : set(["D"])}
    
    graph = { 'A' : set(['B','C']),
             'B' : set(['A','D']),
             'C' : set(['A','D','E']),
             'D' : set(['B','C', 'F']),
             'E' : set(['C','G','H']),
             'F' : set(['D']),
             'G' : set(['E','H']),
             'H' : set(['E','G']) }
    
    bfsST(mygraph, "A")
    print()
    bfsST(graph, "A")\
        
# 출력
# ( A , C )( A , B ) # A가 출발지점이므로 (D, E)는 출력되지 않는다.
# ( A , C )( A , B )( C , E )( C , D )( E , H )( E , G )( D , F )
