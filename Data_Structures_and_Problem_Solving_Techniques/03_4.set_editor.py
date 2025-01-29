#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.21
#######################################

# 집합이란 
# 원소의 중복을 허용하지 않으며 원소들 사이의 순서가 없다는 특징을 가진다.
# 선형 자료 구조가 아니다.

# 집합은 다양한 방법으로 구현할 수 있다.
# 리스트, 비트 벡터, 트리, 해싱구조 등

# 집합의 ADT
# Set() : 비어있는 새로운 집합을 만든다.
# size() : 집합의 원소의 개수를 반환한다.
# contains(e) : 집합이 원소 e를 포함하는 지를 검사하고 반환함
# insert(e) : 새로운 우너소 e를 삽입함. 이미 e가 있다면 삽입하지 않음
# delete(e) : 원소 e를 집합에서 꺼내고(삭제) 반환한다.
# equals(setB) : setB와 같은 집합인지를 검사
# union(setB) : setB와의 합집합을 만들어 반환한다.
# intersect(setB) : setB와의 교집합을 만들어 반환한다.
# difference(setB) : setB와의 차집합을 만들어 반환한다.
# display(): 집합을 화면에 출력한다.

# 집합을 class를 사용한 리스트로 구현
class Set:
    def __init__( self ):
        self.items = []
        
    def size( self ):
        return len(self.items)
    
    def display(self, msg):
        # 메시지와 함께 출력
        print(msg, self.items)
        
    def contains(self, item): # item이 있으면 T, 없으면 F
        for i in range(len(self.items)):
            if self.items[i] == item:
                return True
        return False    
        # 혹은 return item in self.items
    
    def insert(self, elem): 
        if elem not in self.items:
            self.items.append(elem) # 순서가 중요하지 않으니 뒤에 추가
            
    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)
            
    def union( self, setB):
        setC = Set()
        # self리스트를 setC으로 넘길때 캐스팅을 해야지 값이 제대로 전달된다.
        setC.items = list(self.items) 
        
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC        

    def intersect( self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def difference (self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC        
    
# 본문
if __name__ == "__main__":
    setA = Set()
    setA.insert('휴대폰')
    setA.insert('지갑')
    setA.insert('손수건')
    setA.display('SetA :')

    setB = Set()
    setB.insert('빗')
    setB.insert('파이썬 자료구조')
    setB.insert('야구공')
    setB.insert('지갑')
    setB.display('SetB :')

    setB.insert('빗')
    setA.delete('손수건')
    setA.delete('발수건')
    setA.display('Set A:')
    setB.display('Set B:')

    setA.union(setB).display('A U B:')
    setA.intersect(setB).display('A ^ B:')
    setA.difference(setB).display('A - B:')

'''
SetA : ['휴대폰', '지갑', '손수건']
SetB : ['빗', '파이썬 자료구조', '야구공', '지갑']
Set A: ['휴대폰', '지갑']
Set B: ['빗', '파이썬 자료구조', '야구공', '지갑']
A U B: ['휴대폰', '지갑', '빗', '파이썬 자료구조', '야구공']
A ^ B: ['지갑']
A - B: ['휴대폰']
'''
















