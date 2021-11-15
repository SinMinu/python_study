# f-string
name = '홍길동'
age = 20

print(f'안녕하세요 {name}님 나이가{age}살 이군요')

# 2. 문자열.format()
welcome = '환영합니다'
number = 20

print('{}번 손님 {}'.format(number, welcome))

# 예제1
name = '신민우'
color = '초록색'
print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))
print(f'안녕하세요. 제 이름은 {name}이고 좋아하는 색상은 {color}입니다.')


# 문자열 인덱스
print("Hello"[0])

string1 = "abcdefg"
print(string1[2]) # 3번째꺼
print(string1[1:5]) #2~6번까지 
print(string1[::-1]) # -1 역순이라서 뒤에서부터
# 슬라이싱 [시작:끝], [::증감]

# 인덱스 번호로 값으 가져오는것은 가능하지만 수정불가
