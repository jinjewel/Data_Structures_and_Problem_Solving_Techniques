#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.30
#######################################

# 가중치 그래프
# 간선에 가중치가 할당된 그래프
# G = (V, E, w) , w : 비용, 길이 등

# 가중피 그래프의 표현
# 1. 인접행렬을 이용한 표현
# 2. 인접 리스트를 이용한 표현

# 가중치의 총합을 구하기 위한 함수
def weightSum(vlist, W): # 매개 변수 : 정점 리스트, 인접 행렬
    sum = 0 # 가중치 합을 계산할 변수
    for i in range(len(vlist)): # 모든 정점에 대해서 
        for j in range(i+1, len(vlist)): # 하나의 행에 대해서(삼각영역)
            if W[i][j] != None: # 만약 간선이 있으면
                sum += W[i][j] # 합계 변수에 추가
    return sum

# 인접행렬에서 모든 간선을 출력하는 함수
def printAllEdges(vlist, W): # 매개 변수 : 정점 리스트, 인접 행렬
    for i in range(len(vlist)) :
        for j in range(i+1, len(W[i])): # 모든 간선 W[i][j]에 대해
            if W[i][j] != None and W[i][j] != 0: # 간선이 있으면
                print("(%s, %s, %d)"%(vlist[i], vlist[j], W[i][j]), end=" ")
    print()

if __name__ == "__main__":
    # 1. 인접행렬을 이용한 표현
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # 이차원 배열에 인접 행렬을 표시
    weight = [[None, 29, None, None, None, 10, None],
              [29, None, 16, None, None, None, 15],
              [None, 16, None, 12, None, None, None],
              [None, None, 12, None, 22, None, 18],
              [None, None, None, 22, None, 27, 25],
              [10, None, None, None, 27, None, None],
              [None, 15, None, 18, 25, None, None]]
    graph = (vertex, weight) # 전체 그래프: 튜플 사용

    # 인접행렬에서의 가중치의 합 계산
    print('AM : weight sum =', weightSum(vertex, weight))
    print()
    # 인접행렬에서의 모든 간선 출력
    printAllEdges(vertex, weight)

# 출력
# AM : weight sum = 174
#
# (A, B, 29) (A, F, 10) (B, C, 16) (B, G, 15) (C, D, 12) (D, E, 22) (D, G, 18) (E, F, 27) (E, G, 25) 


