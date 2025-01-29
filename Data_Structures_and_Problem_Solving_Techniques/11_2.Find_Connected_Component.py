#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.23
#######################################

## 연결 성분이란
# 최대로 연결된 부분 그래프들을 구함
# DFS 또는 BFS를 반복적으로 이용

def find_connected_component(graph):
    visited = set() # 이미 방문한 정점 집합
    colorList = [] # 부분 그래프별 정점 리스트
    
    for vtx in graph: # 그래프의 모든 정덤들에 대해
        if vtx not in visited: # 방문하지 않은 정점이 있으면
            color = dfs_cc(graph, [], vtx, visited) # 새로운 컬러 리스트
            colorList.append(color) # 컬러리스트에 추가
        
    print("그래프 연결성분 개수 = %d" % len(colorList))
    print(colorList) # 부분 그래프별 정점 리스트 출력

def dfs_cc(graph, color, vertex, visited):
    if vertex not in visited : # 아직 가보지 않은 정점에 대해
        visited.add(vertex) # 전체기준 방문한 리스트에 추가(전역), set이므로 add로 요소를 추가
        color.append(vertex) # 같은 부분기준 방문한 리스트에 추가(지역) 
        nbr = graph[vertex] - visited # 이어진 정점에서 이미 지나간 정점을 뺀 정점저장
        for v in nbr: # 저장된 정점에서 하나씩 
            dfs_cc(graph, color, v, visited) # 순환 호출
    return color # 최종적으로 완성된 부분 정점 그래프 출 

if __name__ == "__main__":
    mygraph = { "A" : set(["B", "C"]),
               "B" : set(["A"]),
               "C" : set(["A"]),
               "D" : set(["E"]),
               "E" : set(["D"])}        

    print('find_connected_component:')
    find_connected_component(mygraph)

# 출력
# find_connected_component:
# 그래프 연결성분 개수 = 2
# [['A', 'C', 'B'], ['D', 'E']]


































