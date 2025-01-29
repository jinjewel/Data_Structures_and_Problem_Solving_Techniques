#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.05
#######################################

# 스택의 응용 : 미로탐색

# 미로 구현 코드
from Stack_class import Stack

def isValidPos(x, y): # 지금의 좌표가 유의한지 검사하는 함수
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE : # 범위 밖이면 False
        return False
    else :
        return map[y][x] == '0' or map[y][x] == 'x' # 0 or x 이면 T, 1이면 F
    
def DFS(): # 깊이우선탐색 함수(Depth Frish Search)
    stack = Stack() # Stack.top = [] 생성
    stack.push( (0,1) ) # 시작위치 삽입, (0,1)은 튜플
    print('DFS:')

    while not stack.isEmpty(): # 공백이 아닐동안
        here = stack.pop() # 최근의 좌표(튜플)을 pop을 통해서 반환
        print(here, end = '->')
        (x, y) = here # 스택에 저장된 튜플을 (x,y) 순서로 표기
        # 켬퓨터는 입력한 값이 열 중심으로 입력되기 때문에 y=-x 대칭으로 인식하여 
        # map[x][y]가 아닌 map[y][x]로 해야 우리가 보는 모습과 같게 위치시킬수 있다.
        if (map[y][x] == 'x'): # 출구면 탐색 성공, T반환
            return True
        else:
            map[y][x] = '.' # 현재 위치를 지나왔다고 '.'표시, 그래야 isValidPos에서 범위 밖으로 판단하여 역주행을 안한다.
            # 4방향의 이웃을 검사해 갈 수 있으면 스택에 상하좌우를 우선순위로 삽입
            if isValidPos(x, y-1):
                stack.push((x, y-1)) # 상
            if isValidPos(x, y+1):
                stack.push((x, y+1)) # 하                
            if isValidPos(x-1, y):
                stack.push((x-1, y)) # 좌               
            if isValidPos(x+1, y):
                stack.push((x+1, y)) # 우  
        print(' 현재스택: ', stack) # 현재 스택 내용 출력      
                
    return False # 탐색 실패, F반환
                
# 본문
if __name__ == "__main__":
    map = [ [ '1', '1', '1', '1', '1', '1'],
           [ 'e', '0', '0', '0', '0', '1'],
           [ '1', '0', '1', '0', '1', '1'],
           [ '1', '1', '1', '0', '0', 'x'],
           [ '1', '1', '1', '0', '1', '1'],
           [ '1', '1', '1', '1', '1', '1']]
    MAZE_SIZE = 6
    result = DFS()

    if result:
        print('--> 미로 탐색 성공')
    else:
        print('--> 미로 탐색 실패')
        
'''
DFS:
(0, 1)-> 현재스택:  [(1, 1)]
(1, 1)-> 현재스택:  [(2, 1), (1, 2)]
(2, 1)-> 현재스택:  [(3, 1), (1, 2)]
(3, 1)-> 현재스택:  [(4, 1), (3, 2), (1, 2)]
(4, 1)-> 현재스택:  [(3, 2), (1, 2)]
(3, 2)-> 현재스택:  [(3, 3), (1, 2)]
(3, 3)-> 현재스택:  [(4, 3), (3, 4), (1, 2)]
(4, 3)-> 현재스택:  [(5, 3), (3, 4), (1, 2)]
(5, 3)->--> 미로 탐색 성공
'''








