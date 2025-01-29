#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.21
#######################################

# 리스트

# 리스트는 가장 자유로운 선형 자료구조 이다.

# 리스크의 구현방법
# 배열의 구조와 연결된 구조로 구현할 수 있다. 

# 리스트, 선형리스트
# 순서를 가진 항목들의 모임 
# 리스트와 달리 집합은 순서가 없는 항목들의 모임이다.

# 리스트의 ADT(추상)
# List() : 비어있는 새로운 리스트를 만든다.
# delete(pos) : pos위치에 있는 요소를 꼬내고(삭제) 반환한다.
# isEmpty() : 리스트가 비어있는지 검사한다.
# getEntry(pos) :  pos 위치에 있는 요소를 반환한다.
# size() : 요소의 갯수를 반환한다.
# clear() : 리스트를 초기화한다.
# find(item) : 리스트에서 item을 찾아 인덱스를 반환한다.
# replace(pos, item) : pos에 있는 항목을 item으로 바꾼다.
# sort() : 정렬
# merge(list) : list를 추가한다.
# display() : 리스트를 화면에 출력한다.
# append(e) : 리스트의 맨 뒤에 새로운 항목을 추가한다.

# 리스크의 내장 매서드
# len(list) : list의 길이를 반환
# list.insert(인덱스, 값) : 인덱스 주소에 값을 삽입한다. 
# list.index(찾을값) : 찾는값이 리스크에 있으면 위치 인덱스를 반환
# list.sort() : 리스트 정렬
# list1.extend(list2) : list1뒤에 list2를 연결한다.
# list.pop(val) : 리스트 안에 val값을 뽑아서 반환하고 삭제한다.

# 배열 구조
# 구현이 간단하며 항목 접근이 O(1)이다.
# 삽입, 삭제시 오버헤드이며 항목의 개수 제한

# 연결된 구조
# 구현이 복잡하며 항목 접근이 O(n)이다.
# 삽입, 삭제가 효율적이며 크기가 제한되지 않는다.

# 자료구조 리스트 : 추상적인 의미에 자료구조 리스트를 말하며 앞에서 ADT를 정의하였다. 
# 이를 구현하기 위해 배열 구조(파이썬 리스트)나 연결된 구조(연결 리스트)를 사용할 것이다.
# 파이썬 리스트 : C언어에서의 배열이 진화된 형태의 스마트한 배열로 배열 구조의 의미로 사용한다.
# 연결리스트 : 자료들이 일렬로 나열 할 수 있는 연결된 구조를 말하여, 배열 구조와 대응되는 의미로 사용한다.

# 파이썬 리스트
# 파이썬 리스트는 스마트한 배열이다.
# 항목을 추가하면서 용량을 자동으로 늘릴수 있다.
# 용량의 오버하는 값을 집어넣으면, 기존의 배열을 복사하여 크기가 2배인 새로운 배열을 만들고 그곳에 대입하고 사용한다.

# 파이썬 리스트의 시간 복잡도
# append(e) : O(1) 
# insert(pos,e) : O(n) 
# pop(pos) : O(n)

# 배열로 구현한 리스트
# 함수 버전 : 전역변수와 함수로 구현

# 함수 선언
items = []

def insert(pos, elem):
    items.insert(pos, elem)
    
def delete(pos):
    return items.pop(pos)

def getEntry(pos):
    return items[pos]

def isEmpty():
    return len(items)==0

def size():
    return len(items)

def clear():
    global items
    items=[]

def find(item):
    return items.index(item)

def replace(pos, elem):
    items[pos] = elem
    
def sort():
    items.sort()

def merge(lst):
    items.extend(lst)

def display(msg='ArrayList: '):
    print(msg, size(), items)    

# 본문

if __name__ == "__main__":
    
    display('파이썬 리스트로 구현한 리스트 테스트')

    # insert(0,10); insert(0,20); insert(1,30); inser(size(),40); insert(2,50)  
    # 한줄로 쓰려면 ;로 문장을 나누면 된다.
    insert(0,10)
    insert(0,20)
    insert(1,30)
    insert(size(),40)
    insert(2,50) 

    display('파이썬 리스트로 구현한 List(삽입*5): ')

    sort()
    display('파이썬 리스트로 구현한 List(정렬후): ')

    replace(2,90)
    display('파이썬 리스트로 구현한 List(교체*1): ')

    delete(2); delete(size()-1); delete(0)
    display('파이썬 리스트로 구현한 List(삭제*3): ')

    lst=[1,2,3]
    merge(lst)
    display('파이썬 리스트로 구현한 List( 병합 ): ')

    clear()
    display('파이썬 리스트로 구현한 List(정리후): ')

'''
파이썬 리스트로 구현한 리스트 테스트 0 []
파이썬 리스트로 구현한 List(삽입*5):  5 [20, 30, 50, 10, 40]
파이썬 리스트로 구현한 List(정렬후):  5 [10, 20, 30, 40, 50]
파이썬 리스트로 구현한 List(교체*1):  5 [10, 20, 90, 40, 50]
파이썬 리스트로 구현한 List(삭제*3):  2 [20, 40]
파이썬 리스트로 구현한 List( 병합 ):  5 [20, 40, 1, 2, 3]
파이썬 리스트로 구현한 List(정리후):  0 []
'''













