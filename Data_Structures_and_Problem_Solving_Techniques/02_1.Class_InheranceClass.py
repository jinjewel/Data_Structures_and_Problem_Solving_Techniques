#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.14
#######################################

# 클래스

# car class 생성
class Car:
    def __init__(self, color, speed = 0): # 생성자 함수
        self.color = color
        self.speed = speed
        
    def speedUp(self): # 멤버 함수 구현
        self.speed += 10
        
    def speedDown(self): # 멤버 함수 구현
        self.speed -= 10
        
    def __eq__(self, carB): # 비교 연산자
        return self.color == carB.color
    
    def __str__(self): # 출력 연산자
        return "color = %s, speed = %d" % (self.color, self.speed)
      
car1 = Car('black', 0)
car2 = Car('red', 120)       
car3 = Car('yellow', 30)
car4 = Car('blue', 0)
car5 = Car('green')
car6 = Car('purple')

car2.speedDown()
car4.speedUp()

car3.color = 'purple'
car5.speed = 100

# 모듈 사용 X
print("car2 == car6 : ", car2 == car6)
print("car3 == car6 : ", car3 == car6)

# 모듈 사용 O
print("car2 == car6 : ", Car.__eq__(car2, car6))
print("car3 == car6 : ", Car.__eq__(car3, car6))

print("[car3]", Car.__str__(car3))

'''
car2 == car6 :  False
car3 == car6 :  True
car2 == car6 :  False
car3 == car6 :  True
[car3] color = purple, speed = 30
'''


# 클래스의 상속
class SuperCar(Car):
    def __init__(self, color, speed=0, bTurbo = True):
        super().__init__(color, speed) # 부모 클래스의 생성자 호출
        self.bTurbo = bTurbo # 터보변수 생성
     
    def setTurbo(self, bTurbo = True):
        self.bTurbo = bTurbo

    def speedUp(self): # 메소드의 재정의
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()
            
    def __str__(self): # 메소드의 재정의
        if self.bTurbo :
            return "[%s] [speed = %d] 터보모드" % (self.color, self.speed)
        else:
            return "[%s] [speed = %d] 일반모드" % (self.color, self.speed)
        
        
s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("white", 0, False)

s1.speedUp()
s2.speedUp()
print("슈퍼카1 : ", s1)
print("슈퍼카2 : ", s2)

'''
슈퍼카1 :  [Gold] [speed = 50] 터보모드
슈퍼카2 :  [white] [speed = 10] 일반모드
'''























