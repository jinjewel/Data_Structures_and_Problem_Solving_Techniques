#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.26
#######################################

# 해싱 : 키 값에 대한 산술적 연산에 의해 테이블의 주소를 계산
# 해시 테이블 : 키 값의 연산에 의해 직접 접근이 가능한 구조, 해시 함수가 키 값을 생성할때 참조하는 테이블
# 버킷 : 하나의 주소를 갖는 파일의 한 구역
# 슬롯 : 한 개의 레코드를 저장 할 수 있는 공간, 한 버킷 안에 여러 개의 슬롯이 있다.
# 충돌 : 서로 다른 키가 해시 함수에 의해 같은 주소로 계산되는 상황. 레코드는 버킷의 다음 슬롯 중 빈곳에 들어가게 된다.
# 동의어 : 충돌이 일어난 레코드의 집합. 키값이 같은 레코드의 집합으로, 동의어가 슬롯의 개수보다 많다면 오버플로우가 생긴다.
# 오버플로 : 한 홈 주소의 버킷 내에 더이상의 레코드를 저장할 슬롯이 없는 상태, 충돌이 슬롯 수보다 많이 발생하는 것
# 해시 함수 : 탐색키를 입력 받아 해시 주소 생성

# 선형 조사에 의한 오버플로 처리, 삽입 연산
# key    45 27 88  9 71 60 46 38 24
# h(key)  6  1 10  9  6  8  7 12 11

# .. 27 .. .. .. .. 45 .. .. 09 88 .. ..
# 00 01 02 03 04 05 06 07 08 09 10 11 12 // 45, 27, 88, 9 대입

# .. 27 .. .. .. .. 45 71 .. 09 88 .. ..
# 00 01 02 03 04 05 06 07 08 09 10 11 12 // 71 대입시 충돌 발생, 다음 슬롯인 07번에 저장

# .. 27 .. .. .. .. 45 71 60 09 88 46 ..
# 00 01 02 03 04 05 06 07 08 09 10 11 12 // 60 대입 후 46 대입시 충돌 발생, 다음 슬롯인 11에 저장

# 24 27 .. .. .. .. 45 71 60 09 88 46 38
# 00 01 02 03 04 05 06 07 08 09 10 11 12 // 38 대입 후 24 대입시 충돌 발생, 다음 슬롯인 00에 저장

# 선형 조사의 탐색 연산
# 순서대로 값을 찾는다.

# 선형 조사의 삭제 연산
# 빈 버킷을 만나면 연산을 정지하므로 앞서서 값이 있다가 삭제된 버킷은 원래 빈 버킷과 다르게 분류하여 표시한다.

# 선형조사 군집화 완화 방법
# 이차 조사법
# 이중 해시법 - 재행싱 방법으로 충동이 발생하면, 다른 해시 함수를 이용해 다음 위치 계산

# 체이닝에 의한 오버플로 처리
# 하나의 버킷에 여러 개의 레코드를 저장 할 수 있도록 하는 방법
# 예) h(k)) = k%7 라는 해시 함수를 이용해 0~7인덱스를 가지는 버킷에 값들을 입력
# 8, 1, 9, 6, 13을 대입할 때, 
# 8과 1은 나머지가 1로 같으므로 충돌 발생 -> 같은 1슬롯에 새로운 노드를 생성하여 순서대로(8 -> 1) 저장
# 6과 13은 나머지가 6로 같으므로 충돌 발생 -> 같은 6슬롯에 새로운 노드를 생성하여 순서대로(6 -> 13) 저장

# 좋은 해시 함수의 조건
# 충돌이 적어야 한다.
# 함수 값이 케이블의 주소 영역 내에서 고르게 분포되어야 한다.
# 계신이 빨라야 한다.

# 제산 함수
# h(k) = k mod M
# 해시 테이블의 크기는 M은 소수(prime number) 선택

# 폴딩 함수 (16바이트 공간에 30바이트 변수를 대입하려고 할때 등 사용)
# 탐색키를 이용하여 이동폴딩, 경계폴딩을 진행할 수 있다.

# 해시함수
# 중간 제곱 함수 : 탐색키를 제곱한 다음, 중간의 몇 비트를 취해서 해시 주소 생성
# 비트 추출 함수 : 키를 이진수로 간주, 임의의 위치의 k개의 비트를 사용

# 탐색 방법들의 성능 비교
# 해싱의 적재 밀도 or 적재 비율 = (저장된 항목의 개수) / M(버킷의 개수)


# 맵의 응용 : 리스트를 이용한 순차탐색 맵
# 맵은 바이너리 이다.

# 나의 단어장
def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i].key == key: # A는 딕셔너리라서 각 인덱션에 들어있는 key 값을 비교하려면 A[i].key로 표현해야 한다.
            return i
    return None

class Entry: # 입력된 key와 value를 딕셔너리로 저장시켜 대입해주는 class 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self): # 출력 지정자도 딕셔너리로 출력을 하도록 지정
        return str("%s:%s" % (self.key, self.value))
    
class SequentialMap:
    def __init__(self):
        self.table = []
        
    def insert(self, key, value):
        self.table.append(Entry(key, value)) # 각 요소에 딕셔너리로 key와 value를 대입한다.
        
    def search(self, key):
        pos = sequential_search(self.table, key, 0, len(self.table)-1)
        if pos is not None: # pos, 즉 key값을 찾으면
            return self.table[pos]
        else: # pos, 즉 key값을 찾지 못하면
            return None
    
    def delete(self, key):
        for i in range(len(self.table)):
            if self.table[i].key == key: # 각 요소에 key값이 일치하면
                self.table.pop(i)
                return
            
    def display(self, msg):
        print(msg)     
        for i in range(len(self.table)):
            print("    ",self.table[i]) # for문으로 돌면서 첫번째 요소(key, value)부터 출력한다.
            
if __name__ == "__main__":
    map = SequentialMap()
    map.insert('data','자료')
    map.insert('structure','구조')
    map.insert('sequential search','선형 탐색')
    map.insert('game','게임')
    map.insert('data','자료')
    map.insert('binary search','이진 탐색')    
    map.display("나의 단어장: ")
    
    print("탐색:game --> ", map.search('game'))
    print("탐색:over --> ", map.search('over'))    
    print("탐색:data --> ", map.search('data'))

    map.delete('game')
    map.display("나의 단어장: ")

'''
나의 단어장: 
     data:자료
     structure:구조
     sequential search:선형 탐색
     game:게임
     data:자료
     binary search:이진 탐색
탐색:game -->  game:게임
탐색:over -->  None
탐색:data -->  data:자료
나의 단어장: 
     data:자료
     structure:구조
     sequential search:선형 탐색
     data:자료
     binary search:이진 탐색
'''



