#######################################
# 정보통계학과 
# 학번 : 2019015020 
# 이름 : 오진석
# 작성일 : 10.26
#######################################

# 맵의 응용 : 딕셔너리를 이용한 구현
# 딕셔너리의 초기형식이 맵이다.

d = {}
d['data'] = '자료'
d['structure'] = '구조'
d['sequential search'] = '선형 탐색'
d['game'] = '게임'
d['binary search'] = '이진 탐색'
print("나의 단어장: ")
print(d)

if d.get('game') : 
    print("탐색:game --> ", d['game'])
if d.get('over') : 
    print("탐색:over --> ", d['over'])     
if d.get('data') : 
    print("탐색:data --> ", d['data'])
    
d.pop('game') # 게임 삭제
print("나의 단어장: ")
print(d)

'''
나의 단어장: 
{'data': '자료', 'structure': '구조', 'sequential search': '선형 탐색', 'game': '게임', 'binary search': '이진 탐색'}
탐색:game -->  게임
탐색:data -->  자료
나의 단어장: 
{'data': '자료', 'structure': '구조', 'sequential search': '선형 탐색', 'binary search': '이진 탐색'}
'''