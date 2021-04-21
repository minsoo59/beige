# print("hello")
# 여기까지 함
# <- 파이썬 주석

# -------------------------------------


a = 3
b = 4
# print(type(a+b))
print(a*b)
print(a//b)  # 몫이 나옴

a = 'Life is too short \n You need python'
# \n : 줄바꿈 \t : 탭사이의 간격 줄때 사용 \\ : 문자 \를 그대로 표현할 때 사용
# \' : 작은따옴표(') \" : 큰따옴표(") """은 여러줄의 문자열 쓸때 좋음

print(a)

a = "Python"
b = " is fun!"
print(a * 100)  # 파이썬에서는 가능함


# 인덱싱
a = 'Life is too short \n You need python'
print(a[0])  # 결과값 L 배열처럼 글자값
print(a[-1])  # 결과값 n

# 슬라이싱 : 문자를 자른다고해서 슬라이싱이라고 부름
c = '123456789'
print(c[0:4])  # 1234 변수[이상:미만:간격]
print(c[:8])  # 12345678 비워두면 무조건 첫번째부터 시작한다는 뜻
print(c[3:])  # 456789
print(c[::2])  # 13579 간격이 2니까

# 문자열 포매팅
e = "I eat " + str(3) + " apples"  # 이걸쓰기 귀찮으니까 아래의 포매팅을 쓴다
d = "I eat %d apples." % 3
print(d)
print(e)
number = 10
day = "three"
i = "I ate %d apples. so I was sick for %s days." % (number, day)  # 여러개 넣을시 괄호
# %s(문자열) %c(문자한개) %d(정수)
print(i)

u = "%0.4f" % 3.4894654654  # %0(간격).4(소수점남기는 자리 수)
print(u)

y = "hobby"
print(y.count('b'))  # count함수는 b가 몇개 들어가 있는지
print(y.find('b'))  # find b가 어디 위치에 있는지 '하나'만 찾아줌 (제일처음꺼)
print(y.index('b'))  # 위치 찾기2
g = ","
print(g.join('hobby'))  # 문자열 삽입
print(y.upper())  # 대문자 바꾸기
print(y.lower())  # 소문자 바꾸기
ff = " hiiiii "
print(ff.strip())  # 문자열 양쪽 공백 지우기
kk = "Life is too short"
print(kk.replace("Life", "Your leg"))  # 문자열 교체
print(kk.split())  # 문자열 나누기(아무것도 안넣으면 띄어쓰기 기준으로 나눠짐)
a = "a:b:c:d"
print(a.split(':'))

# 리스트
# 연속된 범위의 값 수정하기
a = [1, 2, 3]
a[1:2]
# 특정값 삭제하려면 a[1:3] = [] 빈리스트쓰거나 del함수 사용해 리스트 요소 삭제
# append 리스트추가 # sort 리스트 정렬
# reverse 리스트 뒤집기 # index 위치반환
# insert 특정 위치에 요소 삽입 # remove 특정 위치에 요소 삭제
# pop 리스트 요소 끄집어내기(맨 마지막요소) # count 리스트 요소의 개수
# extend 리스트 확장, 추가

# 자료형을 알고있으면 그 언어의 절반을 배운것이다.
