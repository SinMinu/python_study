two_digit_number = input('두 자리 숫자를 입력:\n')
x = two_digit_number[0]
y = two_digit_number[1]
z = int(x) + int(y)
print(f'{x}+{y}={z}')


height = input("키를 미터 단위로 입력하세요 : ")
weight = input("몸무게를 킬로 단위로 입력하세요 : ")

BMI = float(weight) / float(height)**2
print(f'당신의 bmi는 {round(BMI,2)}입니다.')