#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.14
#######################################
 
# 파이썬이란

# 파이썬의 예약어 (yield, nonlocal, del 등)
# 자료형(수치, 시퀀스, 매핑, 집합)과 리터럴(자료형에 대한 값)
# 수치(int, float, complex, bool)
# 시퀀스(str, list, tuple) 
# 매핑(dict) 
# 집합(set) 

#  키보드 입력과 출력 함수

name = input("당신의 이름을 입력하세요.")
habby = input("취미가 무엇입니까?")
age = int(input("나이가 몇살 입니까?"))
score = float(input("평균학점이 얼마입니까?"))

print("\ninput over", end=" ")
print("\n%s의 취미는 %s이고 나이는 %d이며 평균학점은 %f임니다.\n" % (name, habby, age, score))

'''
당신의 이름을 입력하세요.jinseok
취미가 무엇입니까?study
나이가 몇살 입니까?24
평균학점이 얼마입니까?4.12

input over 
jinseok의 취미는 study이고 나이는 24이며 평균학점은 4.120000임니다.
'''