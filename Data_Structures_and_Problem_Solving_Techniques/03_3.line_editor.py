#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.21
#######################################

# 리스트의 응용 : 라인편집기

# 라인 편집기의 기능
# i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료

from Array_list_class import ArrayList

def myLineEditor(): # 라인 편집기 주 함수
    
    list = ArrayList() # ArrayList() 객체 list 생성
    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> ")
        
        if command =='i': # 삽입 연산
            pos = int(input("입력행 번호 :"))
            str = input("입력할 내용: ")
            list.insert(pos, str) # insert 메소드로 삽입
            
        elif command == 'd': # 행 삭제
            pos = int(input("삭제행 번호 :"))
            list.delete(pos) # delete 메소드로 삭제
            
        elif command == 'r': # 행 변경
            pos = int(input("변경행 번호 :"))
            str = input("변경할 내용: ")
            list.replace(pos, str) # replace 메소드로 변경
            
        elif command == 'p':
            print("line editor")
            for line in range(list.size()): # size 메소드로 크기 구하기
                print('[%2d] ' % line, list.getEntry(line)) # getEntry 메소드로 단순 값 반환
            print()    
                
        elif command == 'q':  
            return
                
        elif command == 'l':  
            filename = input(" 읽어들일 파일 이름: ")
            infile = open(filename, "r")
            lines = infile.readlines();
            for line in lines:
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()    
            
        elif command == 's':    
            filename = input("저장할 파일 이름: ")
            openfile = open(filename, 'w')
            for i in range(list.size()):
                openfile.write(list.getEntry(i)+'\n')
            openfile.close()  
            
        elif command == 'f':
            str = input("칮는 문자열: ")
            for line in range(list.size()):
                if list.getEntry(line).find(str) >= 0:
                    print(list.getEntry(line))

# 본문
if __name__ == "__main__":
    myLineEditor()

'''
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> l
 읽어들일 파일 이름: text.txt
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> p
line editor
[ 0]  class ArrayList:
[ 1]      def __init__(self):
[ 2]          self.items=[]
[ 3]          
[ 4]      def insert(self, pos, elem) : self.items.insert(pos, elem)
[ 5]      def delete(self, pos) : return self.items.pop(pos)
[ 6]      def getEntry(self, pos) : return self.items[pos]

[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> r
변경행 번호 :5
변경할 내용:     def delete(this, pos) : this.items.pop(pos)
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> p
line editor
[ 0]  class ArrayList:
[ 1]      def __init__(self):
[ 2]          self.items=[]
[ 3]          
[ 4]      def insert(self, pos, elem) : self.items.insert(pos, elem)
[ 5]      def delete(this, pos) : this.items.pop(pos)
[ 6]      def getEntry(self, pos) : return self.items[pos]

[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> q
'''

'''
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> i
입력행 번호 :0
입력할 내용: contents
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> i
입력행 번호 :1
입력할 내용: 자료구조와 알고리즘
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> i
입력행 번호 :2
입력할 내용: 리스트
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> i
입력행 번호 :3
입력할 내용: 스택, 큐, 덱
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> p
line editor
[ 0]  contents
[ 1]  자료구조와 알고리즘
[ 2]  리스트
[ 3]  스택, 큐, 덱

[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> d
삭제행 번호 :1
[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> p
line editor
[ 0]  contents
[ 1]  리스트
[ 2]  스택, 큐, 덱

[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료=> q
'''




