#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 09.14
#######################################


# 문자열(str)
msg = 'game over'
hi = "hello world"
sum = "예전엔" + hi + "이제는" + msg
print(sum)

print(msg, '의 첫 글자는 ', msg[0])
print(msg, '의 끝 글자는 ', msg[-1])

hobby = "테니스"
age = 21 
score =  4.5
msg1 = "당신의 학점은 %4.1f입니다." % score
msg2 = "취미=%s, 나이=%d, 학점=%f" % (hobby, age, score)
print(msg1)
print(msg2)

'''
예전엔hello world이제는game over
game over 의 첫 글자는  g
game over 의 끝 글자는  r
당신의 학점은  4.5입니다.
취미=테니스, 나이=21, 학점=4.500000
'''

# 리스트(list)

# append(item)
# extend(lst)
# count(item)
# index(item, 시작, 종료) : 시작부터 종료까지 item이 있는 곳의 가장작은 인덱스를 반환
# insert(pos, item) : pos위치에 item를 삽입한다.
# pop(pos) : pos 위치에 항목 item을 삽입한다.
# remove(itme)
# reverse()
# sort([key])

big3 = []
lotto = [23, 34, 11 , 42, 9]
big4 = ['제이플라', '도티', '대도서관', '보람튜브']

print("lotto[1] = ",lotto[1])
big4[2] = '블랙핑크'
big3.append("알라딘")
big3.append("엘사")
big3.append("안나")

'''
lotto[1] =  34
'''

# 튜플(tuple)

# 리스트와 동일하지만 크기나 값을 변경할 수 없다.
# 메모리는 효율적으로 사용가능

t = (0, 3, 7)
a = (2)
b = ('game' , 1 , 3.14 , 2019)

print("취미=%s, 나이=%d, 학점=%f " % (hobby, age, score))

'''
취미=테니스, 나이=21, 학점=4.500000 
'''

# 딕셔너리(dict)

# 키와 관련된 값으로 이루어진 항목들의 집합
map = {'김연아':'피겨', '쿠드롱':'당구', '메시':'축구'}
print(map)
print("쿠드롱이 뭐하는 사람이지?", map['쿠드롱'])

map['나달'] = '테니스'
map.update({'최민영':'여자야구' , '고진영':'골프'})
print(map)

'''
{'김연아': '피겨', '쿠드롱': '당구', '메시': '축구'}
쿠드롱이 뭐하는 사람이지? 당구
{'김연아': '피겨', '쿠드롱': '당구', '메시': '축구', '나달': '테니스', '최민영': '여자야구', '고진영': '골프'}
'''

# 셋(set)
s1 = {1,2,3}
s2 = {2,3,4,5}
s3 = s1.union(s2)
s4 = s1.intersection(s2)
s5 = s1 - s2

print("s1 : ", s1)
print("s2 : ", s2)
print("s3 : ", s3)
print("s4 : ", s4)
print("s5 : ", s5)

s5 = { 31.4}
map = { 3.14 : 'phi'}

'''
s1 :  {1, 2, 3}
s2 :  {2, 3, 4, 5}
s3 :  {1, 2, 3, 4, 5}
s4 :  {2, 3}
s5 :  {1}
'''



