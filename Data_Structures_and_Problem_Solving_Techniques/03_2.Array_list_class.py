#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.21
#######################################

# 배열로 구현한 리스트
# 클래스 버전 : 클래스 변수 선언 및 초기화

class ArrayList:
    
    def __init__(self): # 생성자
        self.items=[]
        
    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos):
        return self.items.pop(pos)

    def getEntry(self, pos):
        return self.items[pos]

    def isEmpty():
        return self.size()==0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items=[]

    def find(self, item):
        return self.items.index(item)

    def replace(self, pos, elem):
        self.items[pos] = elem
        
    def sort(self):
        self.items.sort()

    def merge(self, lst):
        self.items.extend(lst)

    def display(self, msg='ArrayList: '):
        print(msg, '항목수=', self.size(), self.items)    

# 본문 출력
if __name__ == "__main__": 
    s = ArrayList()

    s.display('파이썬 리스트로 구현한 리스트 테스트')

    s.insert(0,10); s.insert(0,20); s.insert(1,30)
    s.insert(s.size(),40); s.insert(2,50)  

    # s.display('파이썬 리스트로 구현한 List(삽입*5): ')
    s.display('파이썬 리스트로 구현한 List(삽입*5): ') 

    s.sort()
    s.display('파이썬 리스트로 구현한 List(정렬후): ')

    s.replace(2,90)
    s.display('파이썬 리스트로 구현한 List(교체*1): ')

    s.delete(2); s.delete(s.size()-1); s.delete(0)
    s.display('파이썬 리스트로 구현한 List(삭제*3): ')

    lst=[1,2,3]
    s.merge(lst)
    s.display('파이썬 리스트로 구현한 List( 병합 ): ')

    s.clear()
    s.display('파이썬 리스트로 구현한 List(정리후): ')
    
'''
파이썬 리스트로 구현한 리스트 테스트 항목수= 0 []
파이썬 리스트로 구현한 List(삽입*5):  항목수= 5 [20, 30, 50, 10, 40]
파이썬 리스트로 구현한 List(정렬후):  항목수= 5 [10, 20, 30, 40, 50]
파이썬 리스트로 구현한 List(교체*1):  항목수= 5 [10, 20, 90, 40, 50]
파이썬 리스트로 구현한 List(삭제*3):  항목수= 2 [20, 40]
파이썬 리스트로 구현한 List( 병합 ):  항목수= 5 [20, 40, 1, 2, 3]
파이썬 리스트로 구현한 List(정리후):  항목수= 0 []
'''





















