# 입력, 출력이 없을 수도 있음.
def sum(a, b):
    result = a + b
    return result


print(sum(1, 2))

# 함수라는게 입력값과 출력값이 무조건 있어야하는건 아니다!


def say():
    return "hi!"  # 입력값 X


print(say())


def sum2(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))  # 결과값 X


sum2(1, 2)


# 입력값(인자)를 여러개 받을 때 *args를 쓰면 굳이 숫자에 맞춰 하나하나 지정할 필요가 없다.
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


print(sum_many(1, 2, 3))

# **kwags


def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print('당신의 이름은 : ' + k)


print(print_kwargs(name="int 조수", b="2"))

# 함수의 리턴값은 언제나 하나이다. 튜플형태로 나옴


def sum_and_mul(a, b):
    return a+b, a*b, a-b


print(sum_and_mul(1, 2)[0])  # 리턴값 중 0번째값만 쓸래 할 경우


# 초기값 미리 설정하기
# 세번째 값을 true라고 미리 설정할 경우 안 넣어라도 기본적으로 true라고 설정이 된다.
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("라이유튜브", 20)

# 함수 안에서 선언된 변수의 효력범위
a = 1


def vartest():
    global a  # 글로벌 범위의 함수설정
    a = a+1


vartest()
print(a)

# Lambda


def add(a, b):
    return a+b


# add = lambda a, b: a+b
 # 위에랑 동일함.
print(add(1, 2))

myList = [lambda a, b:a+b, lambda a, b: a*b]
print(myList[1](2, 2))  # 함수를 편리하게 정의하고 은근히 많이씀

# a = input("숫자를 입력하세요")  # 외장함수 : 사전에 이미 정해져있는 함수
print(a)

for i in range(10):
    print(i, end=' ')  # end를 쓰면 한줄에 하나씩이 아니라 띄어쓰기 형식으로 출력됨.

# w는 쓰기모드 r은 읽기 모드 a는 추가모드(파일 마지막에 새로운내용을 추가시킬때)
# 파일 쓰기
f = open("C:/Users/minsu/Documents/GitHub/python/새파일.txt", 'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

# 읽기 1
f = open("C:/Users/minsu/Documents/GitHub/python/새파일.txt", 'r', encoding="UTF-8")
line = f.readline()  # 파일이 있으면 한줄씩 읽어오는 함수
print(line)
f.close()  # 항상 닫아야함.

# 읽기 2
f = open("C:/Users/minsu/Documents/GitHub/python/새파일.txt", 'r', encoding="UTF-8")
# 무한반복 while
while True:
    line = f.readline()  # 파일이 있으면 한줄씩 읽어오는 함수
    if not line:
        break
    print(line)
f.close()  # 항상 닫아야함.

# 읽기 3
f = open("C:/Users/minsu/Documents/GitHub/python/새파일.txt", 'r', encoding="UTF-8")
lines = f.readlines()  # readlines는 리스트형태로 가져와서 출력하는것
for line in lines:
    print(line.strip("\n"), end="")  # 한칸 띄어쓰기
f.close()  # 항상 닫아야함.

# 읽기 4
f = open("C:/Users/minsu/Documents/GitHub/python/새파일.txt", 'r', encoding="UTF-8")
data = f.read()  # 통채로 다 읽어서 쓰는것.
print(data)
f.close()

# 파일 내용 추가하기
f = open("C:/Users/minsu/Documents/GitHub/python/새파일.txt", 'a', encoding="UTF-8")
for i in range(11, 21):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()

# with문(이걸 쓰면 close를 안써도 됨)
with open("C:/Users/minsu/Documents/GitHub/python/새파일.txt", "w") as f:
    f.write("Life is too short, you need python")
