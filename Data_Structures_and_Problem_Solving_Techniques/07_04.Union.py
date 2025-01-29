#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.26
#######################################

# 비교연산

# 3장에서 구현한 집합 자료구조 수정하기
# 집합의 원소들을 항상 정렬된 순으로 저장
# 삽입 연산은 더 복잡해 짐
# 집합의 비교나 합집합, 차집합, 교집합 -> 효율적 구현 가능

# 집합에 원소 삽입, 같은집합찾기, 합집합, 차집합, 교집합에 복잡도 비교
# insert(e)         정렬되지않음: O(n)   /  정렬됨: O(n)
# __eq__(setB)      정렬되지않음: O(n^2) /  정렬됨: O(n)
# union(setB)       정렬되지않음: O(n^2) /  정렬됨: O(n)
# intersect(setB)   정렬되지않음: O(n^2) /  정렬됨: O(n)
# difference(setB)  정렬되지않음: O(n^2) /  정렬됨: O(n) 

class Sort:
    
    def insert(self, elem): # 정렬된 상태를 유지하면서 elem을 삽입
        
        if elem in self.items: # 삽입하려는 값이 이미 집합에 있으면
            return # 삽입 중단
            
        for idx in range(len(self.items)): # 0부터 집합의 크기-1까지의 수를 대입
            if elem < self.items[idx]: # 왼쪽부터(작은값) 비교하다가 삽입하려는 값보다 큰 값이 나오면
                self.items.insert(idx, elem) # 그 위치에 삽입하려는 값을 대입한다.
                return
        self.items.append(elem) # 집합에 삽입하려는 값보다 큰 값이 없다면 맨 오른쪽에 추가한다.
    
    def __eq__(self, set):
        if self.size() != setB.size(): # 두 집합의 크기가 다르면 같지 않다.
            return False
        for idx in range(len(self.items)): # 두 집합의 크기만큼 반복을 한다.
            if self.items[idx] != setB.items[idx]: # 각 인덱스 위치에 값들을 비교
                return False
        return True
    
    def union(self. setB):
        newSet = Set() # 두 집합의 합집합을 저장하는 공간
        a = 0
        b = 0
        # 비교하는 집합의 인덱스가 두 집합의 길이가 보다 작을때만 반복 
        while a < len(self.items) and b < len(setB.items): 
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB:
                newSet.items.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet.items.append(valueB)
                b += 1
            else:
                newSet.items.append(valueA)
                a += 1
                b += 1
        # 반복이 끝났을 때, self.items의 집합 남았으면, 즉 a의 인덱스가 오버가 안됬으면
        while a < len(self.items): 
            newSet,items.append(self.items[a])
            a += 1
        # 반복이 끝났을 때, setB.items의 집합 남았으면, 즉 b의 인덱스가 오버가 안됬으면    
        while b < len(setB.items):
            newSet.items.append(setB.items[b])
            b += 1
        return newSet
    
# 알고리즘
# step=0 newSet                     # step=5 newSet 0 1 2 3 4
# a=0 self.items 0 1 2 5            # a=3 self.items 0 1 2 5
# b=0 setB.items 1 2 3 4 5 6 7      # b=4 setB.items 1 2 3 4 5 6 7
#                                   #
# step=1 newSet 0                   # step=6 newSet 0 1 2 3 4 5
# a=1 self.items 0 1 2 5            # a=4(종료) self.items 0 1 2 5
# b=0 setB.items 1 2 3 4 5 6 7      # b=5 setB.items 1 2 3 4 5 6 7  
#                                   #
# step=2 newSet 0 1                 # step=7 newSet 0 1 2 3 4 5 6
# a=2 self.items 0 1 2 5            # a=4(종료) self.items 0 1 2 5
# b=1 setB.items 1 2 3 4 5 6 7      # b=6 setB.items 1 2 3 4 5 6 7
#                                   #
# step=3 newSet 0 1 2               # step=8 newSet 0 1 2 3 4 5 6 7
# a=3 self.items 0 1 2 5            # a=4(종료) self.items 0 1 2 5
# b=2 setB.items 1 2 3 4 5 6 7      # b=7(종료) setB.items 1 2 3 4 5 6 7  
#                                   
# step=4 newSet 0 1 2 3
# a=3 self.items 0 1 2 5
# b=3 setB.items 1 2 3 4 5 6 7




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    