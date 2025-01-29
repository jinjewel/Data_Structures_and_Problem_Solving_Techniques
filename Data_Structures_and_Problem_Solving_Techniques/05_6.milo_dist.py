#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.12
#######################################

# 전략적 미로 탐색(알고리즘)

# 도착지점을 알 경우 점과 점사이의 거리를 사용하여 갈림길 중 좀더 가까운 쪽부터 먼저 계산하는 알고리즘
from PriorityQueue import PriorityQueue
from math import *

def dist(a, b): # 거리계산 함수
    return sqrt((5-a)*(5-a) + (4-b)*(4-b))*(-1)

def isValidPos(x, y):
    if x<0 or y<0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'
    
def findMaxIndex( self ): # 부모의 함수를 재정의
    if self.isEmpty():
        return None
    else:
        highest = 0
        for i in range( 1, self.size()):
            if self.items[i][2] > self.items[highest][2]:
                highest = i
    return highest           

def MySmartSearch() :
    q = PriorityQueue() # q.items = [] 생성
    q.enqueue((0,1,dist(0,1))) # 순서가 필요없으므로 차례대로 대입, dist는 도착점까지의 거리를 반환하는 함수이다.
    print('PQueue: ')
    
    while not q.isEmpty(): # 비어있지 않으면
        here = q.dequeue() # 재정의된 findMaxIndex를 통해 가장 위에 있는 좌표와 거리의 튜플를 대입 후 삭제
        x, y, _ = here # -를 사용하여 dist 값은 버린다.
        print(here[0:2], end="->") # 거리를 제외한 'X,Y' 만 출력하기 위해 0:2로 출력
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.' # 지나간 점 '.'으로 표기
            # 컴터는 열을 기준으로 값을 대입하므로 눈에 보이는 지도와 인댁스가 y=-x 대칭이다.
            # 따라서 [x][y] 가 아닌 [y][x]로 생성
            if isValidPos(x, y-1): # 움직인 점이 T이면(0 또는 x) 실행
               q.enqueue((x, y-1, dist(x, y-1))) # 상, 만약 [x][y]이였다면, (x-1, y)
            if isValidPos(x, y+1): # 움직인 점이 T이면(0 또는 x) 실행
               q.enqueue((x, y+1, dist(x, y+1))) # 하, 만약 [x][y]이였다면, (x+1, y)                
            if isValidPos(x-1, y): # 움직인 점이 T이면(0 또는 x) 실행
               q.enqueue((x-1, y, dist(x-1, y))) # 좌, 만약 [x][y]이였다면, (x, y-1)                
            if isValidPos(x+1, y): # 움직인 점이 T이면(0 또는 x) 실행
               q.enqueue((x+1, y, dist(x+1, y))) # 우, 만약 [x][y]이였다면, (x, y+1) 
        # 갈림길에서 막히는 부분은 멈추고, 길이 있는 부분은 계속 갱신되는 방식으로 튜플이 연속해서 출력       
        print('우선순위큐: ', q.items) 
    return False         

# 본문
if __name__ == "__main__":
    
    MAZE_SIZE = 6
    map = [['1', '1', '1', '1', '1', '1'], 
           ['e', '0', '1', '0', '0', '1'], 
           ['1', '0', '0', '0', '1', '1'], 
           ['1', '0', '1', '0', '1', '1'], 
           ['1', '0', '1', '0', '0', 'x'],
           ['1', '1', '1', '1', '1', '1'] ]
           
    # 경로 탐색
    result = MySmartSearch()
    
    # 결과 출력
    if result:
        print('--> 미로탐색 성공')
    else:
        print('--> 미로탐색 실패')
'''
PQueue: 
(0, 1)->우선순위큐:  [(1, 1, -5.0)]
(1, 1)->우선순위큐:  [(1, 2, -4.47213595499958)]
(1, 2)->우선순위큐:  [(1, 3, -4.123105625617661), (2, 2, -3.605551275463989)]
(2, 2)->우선순위큐:  [(1, 3, -4.123105625617661), (3, 2, -2.8284271247461903)]
(3, 2)->우선순위큐:  [(1, 3, -4.123105625617661), (3, 1, -3.605551275463989), (3, 3, -2.23606797749979)]
(3, 3)->우선순위큐:  [(1, 3, -4.123105625617661), (3, 1, -3.605551275463989), (3, 4, -2.0)]
(3, 4)->우선순위큐:  [(1, 3, -4.123105625617661), (3, 1, -3.605551275463989), (4, 4, -1.0)]
(4, 4)->우선순위큐:  [(1, 3, -4.123105625617661), (3, 1, -3.605551275463989), (5, 4, -0.0)]
(5, 4)->--> 미로탐색 성공
'''




