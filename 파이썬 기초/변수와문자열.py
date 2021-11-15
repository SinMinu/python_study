'''
# 여러개의 변수를 동시에 초기화
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# 예제 2~5 풀기
x = 10
print(x)

x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

x, y, z = 1, 1.1, "문자"
print(type(x))
print(type(y))
print(type(z))

a= input("a: ")
b= input("b: ")
a, b = b, a
print("a: " +a)
print("b: " +b)

'''
# 문자열

# 긴 문자열은 따옴표 3개(''',""")
var3 = '''
따옴표 3개는
끝나는 문장까지 모두를 문자열로 처리
--------------------!
'''

print(var3)

# 문자열 (+) 연산
성 = '홍'
이름 = '길동'
name = 성 + ' ' + 이름

print(name)

# 타입 변환 : str(), int(), float()

print(type(int(str(100))))


# 예제1
str1 = '\tIt\'s "kind of" sunny\n Have a nice Day!'

print(str1)


# 예제2
#string1을 선언하세요.
string1 = '''
"내가 니 애비다!"
'''

print(string1)

# 예제3
print('밴드 이름 만들기 프로그램에 환영합니다.')
a = input('태어난 도시가 어딘가요?\n')
b = input('애완 동물의 이름은?\n')
print('당신의 밴드이름은 '+a+''+b)