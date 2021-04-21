# 리스트 a=[] vs 튜플 b=()
# 리스트는 변경가능하지만, 튜플은 변경불가능.
t1 = (1, 2, 'a', 'b')
# del t1[0]

# 딕셔너리 (자세히 알아야함!) 연관배열이라고도 함. key를 통해 value를 얻는다.
# py->Hash Js->Object

dic = {'name': 'Eric', 'age': 15}
print(dic['name'])

# 추가
a = {1: 'a'}
a['name'] = '익명'

# 삭제
del a[1]  # key를 입력해야함
print(a)

# key가 중복되면 안됨
a = {1: 'a', 1: 'b'}

# 키만 따로뽑을수도 있음
print(a.keys())
print(a.values())
print(a.items())
# for문 쓸때 많이 씀

# 모두 지우기
a.clear()
print(a)


# 집합
#  중복된 요소를 가질 수 없음.
#  순서가 없다(unordered)

# s1 = set[1, 2, 3]
s1 = {1, 2, 3}
print(type(s1))

# 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)  # s1.intersection(s2)

# 합집합
print(s1 | s2)  # s1.union(s2)

# 차집합
print(s1 - s2)  # s1.difference(s2)

# 집합 추가
s1.add(7)
print(s1)
s1.update([8, 9, 0])  # 여러개 추가
print(s1)

# 제거
s1.remove(1)
print(s1)

# bool(boolean)
a = True
print(type(a))

# call stack이 안쓰임(js랑 다르게)
a = [1, 2, 3]
b = a
a[1] = 4
print(a)  # 1, 4, 3
print(b)  # 1, 4, 3 -> 둘다 바뀜
# 만약 복사해서 넣고 싶다면
b = a[:]  # copy(a)
print(a)
print(b)

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')

print(a)
print(b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)
