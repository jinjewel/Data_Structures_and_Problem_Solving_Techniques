#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 11.30
#######################################

## 2. 인접리스트를 이용한 방법

# 가중치의 총합을 구하기 위한 함수
def weightSum(graph):
    sum = 0
    for v in graph: # 그래프의 모든 정점 v에 대해
        for e in graph[v]: # v의 모든 간선 e에 대해 e=('F',10) , ('B',29) , ("G",15) , ... 순서로 각 set에서 거꾸러 출력된다.
            sum += e[1] # sum에 추가
    return sum // 2 # 모두 2번씩 중복 되므로 2로 나눈다.

# 인접행렬에서 모든 간선을 중복을 허용하며 출력하는 함수
def printAllEdges(graph):
    for v in graph: # 그래프의 모든 정점 v에 대해
        for e in graph[v]: # v의 모든 간선 e에 대해
            print("(%s, %s, %d)"%(v, e[0], e[1]), end=' ') # end=' '은 자동 줄바꿈을 띄어쓰기로 바꿔줌
            
 # 인접행렬에서 모든 간선을 중복을 허용하지 않으며 출력하는 함수
def printOneEdges(graph):
    list= []
    for v in graph:
        for e in graph[v]:
            if (v, e[0]) not in list:
                print("(%s, %s, %d)"%(v, e[0], e[1]), end=' ')  
                list.append((v, e[0]))
                list.append((e[0], v))
            
if __name__ == "__main__":
    # 2. 인접 리스트를 이용한 표현
    # 딕셔너리, 집합, 리스트, 튜플 사용
    graphAL = { 'A' : set([('B',29),('F',10)]),
             'B' : set([('A',29),('C',16),('G',15)]),
             'C' : set([('B',16),('D',12)]),
             'D' : set([('C',12),('E',22),('G',18)]),
             'E' : set([('D',22),('F',27),('G',25)]),
             'F' : set([('A',10),('E',27)]),
             'G' : set([('B',15), ('D',18),('E',25)])}
    
    print('AL : weight sum = ', weightSum(graphAL))
    print()
    printAllEdges(graphAL)   
    print("\n\n")
    printOneEdges(graphAL)

    for i in range(5):
        print(i , end= ' ')
# 출력
# AL : weight sum =  174
#
# (A, F, 10) (A, B, 29) (B, G, 15) (B, A, 29) (B, C, 16) (C, D, 12) (C, B, 16) (줄바꿈)
# (D, C, 12) (D, E, 22) (D, G, 18) (E, G, 25) (E, F, 27) (E, D, 22) (F, E, 27) (줄바꿈)
# (F, A, 10) (G, E, 25) (G, B, 15) (G, D, 18) 
#
#
# (A, F, 10) (A, B, 29) (B, G, 15) (B, C, 16) (C, D, 12) (D, E, 22) (D, G, 18) (E, G, 25) (E, F, 27) 













