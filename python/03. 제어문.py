money = 2000

if money > 3000:
    print("Go to take a taxi!")
else:
    print("walk to")


# or = | -> 둘 중하나라도 참이 있으면 True
# and = & -> 둘다 True여야 True 하나라도 False라면 False
# not -> 반대의 의미

# if 1 in [1,2,3]: -> 리스트안에 1이 있냐의 유무
# if 1 not in [1,2,3]: -> 리스트안에 1이 없냐

# pass -> 해당조건이어서 실행되야하지만 넘기고 싶을때
# elif(else if)

scroe = 70
# if scroe >= 60:
#     message = "success"
# else:
#     message = "failure"
# 조건부 표현식(삼항연산자의 파이썬식 표현)
message = "success" if scroe >= 60 else "failure"
print(message)

# while 문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("You hit the tree %d." % treeHit)
    if treeHit == 10:
        print("The tree is over ")

# break -> 반복문을 빠져나가는 구문
# contirue -> while문 안쪽의 문장을 쭉 수행하다가 contirue를 만나게 되면 밑에 문장을 실행하지않고 다시 while의 처음으로 돌아간다.
# Ctrl + C -> 무한루프 종료방법

# for 문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
a = [(1, 2), (3, 4), (5, 6)]
for (frist, last) in a:
    print(frist, last)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

sum = 0
for i in range(1, 11):  # 1이상 11미만으로 뺄수있다는 의미
    print(i)
    sum = sum + i
print(sum)

for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print('')

# =======================================

# result = [num * 3 for num in a if num % 2 == 0]
# result = []
# for num in a:
#     if num % 2 == 0:
#         result.append(num*3)
