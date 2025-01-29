#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.26
#######################################

# 체이닝에 의한 오버플로 처리
# 하나의 버킷에 여러 개의 레코드를 저장 할 수 있도록 하는 방법
# 예) h(k)) = k%7 라는 해시 함수를 이용해 0~7인덱스를 가지는 버킷에 값들을 입력
# 8, 1, 9, 6, 13을 대입할 때, 
# 8과 1은 나머지가 1로 같으므로 충돌 발생 -> 같은 1버킷에 새로운 노드를 생성하여 순서대로(8 -> 1) 저장
# 6과 13은 나머지가 6로 같으므로 충돌 발생 -> 같은 6버킷에 새로운 노드를 생성하여 순서대로(6 -> 13) 저장

# 앱의 응용 : 채이닝을 이용한 해시 맵
# 나의 단어장

from SequentialMap import Entry

class Node:
    def __init__(self, data, link=None): # 생성자
        self.data = data
        self.link = link
        
    def __str__(self): # 출력지정자
        return str("%s:%s" % (self.key, self.value))

class HashChainMap:
    def __init__(self, M):
        self.table = [None]*M # 입력받은 버킷의 수(M)만큼 공간 생성
        self.M = M
        
    def hashFn(self, key):
        sum = 0
        for c in key:          # 문자열의 모든 문자에 대해
            sum = sum + ord(c) # 그 문자의 아스키 코드 값을 sum에 더함
        return sum % self.M    # M으로 나눠서 M크기의 버킷에 알맞은 배정 인덱스를 구한다. 

    def insert(self, key, value):
        idx = self.hashFn(key) # 해당 key값이 어느 버킷에 해당되는지 해시함수를 통해 찾는다.
        # 찾은 버킷에 노드 형식으로 데이터부분에 딕셔너리로 묶은 key와 value를, 링크 부분에 버킷을 넣는다.
        self.table[idx] = Node(Entry(key, value), self.table[idx]) 
        # entry = Entry(key, value) 위에 식을 아래와 같이 여러 줄로 표현 가능
        # node = Node(entry)
        # node.link = self.table[idx]
        # self.table[idx] = node         
        
    def delete(self, key):
        idx = self.hashFn(key) # key가 해당되는 버킷 인덱스 반환받기
        node = self.table[idx] # 해당 인덱스의 버킷 해드를 저장
        before = None
        while node is not None: # 노드가 빈 값일때까지 반복
            if node.data.key == key: # 해당 노드의 data부분의 key값이 찾는 key값과 같으면
                if before == None: # 버킷에 노드가 자기 자신 밖에 없으면
                    self.table[idx] = node.link 
                else: # 버킷에 노드가 2개 이상 있는 경우
                    before.link = node.link
                return
            before = node # 이전에 링크에 현재 링크 노드를 저장
            node = node.link # 노드에 다음 노드 링크를 저장
            
    def search(self, key):
        idx = self.hashFn(key) # key가 해당되는 버킷 인덱스 반환받기
        node = self.table[idx] # 해당 인덱스의 버킷 해드를 저장
        while node is not None: # 노드가 비어 있을 때까지 반복
            if node.data.key == key: # 해당 노드의 data부분의 key값이 찾는 key값과 같으면 
                return node.data # 값 반환
            node = node.link # 같지 않으면 다음 노드 링크를 현재 노드에 저장
        
    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d] -> " % (idx) , end='' )
                while node is not None:
                    print(node.data, end=' ->' )
                    node = node.link
                print()
                
if __name__ == "__main__":
    
    map = HashChainMap(13)
    map.insert('data','자료')
    map.insert('structure','구조')
    map.insert('sequential search','선형 탐색')
    map.insert('game','게임')
    map.insert('binary search','이진 탐색')    
    map.display("나의 단어장: ")
    
    print("탐색:game --> ", map.search('game'))
    print("탐색:over --> ", map.search('over'))    
    print("탐색:data --> ", map.search('data'))

    map.delete('game')
    map.display("나의 단어장: ")
    
'''
[ 3] -> sequential search:선형 탐색 ->
[ 7] -> binary search:이진 탐색 ->game:게임 ->data:자료 ->
[ 8] -> structure:구조 ->
탐색:game -->  game:게임
탐색:over -->  None
탐색:data -->  data:자료
나의 단어장: 
[ 3] -> sequential search:선형 탐색 ->
[ 7] -> binary search:이진 탐색 ->data:자료 ->
[ 8] -> structure:구조 ->
'''


