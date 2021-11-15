# while 반복문
# while True:
#     print("무한반복")

# count = 0
# while count < 3 :
#     print('횟수: ', count)
#     count +=1

# name = ''
# while name != '펭수' :
#     name = input("펭수를 입력해 주세요 :")
# print('Thank you!')

# hit = 0
# while hit < 10 : 
#     hit += 1
#     if hit % 2 == 0 : # hit가 짝수이면 아래코드는 실행하지 않고 다시 조건으로
# #         continue
# #     print(f'나무를 {hit}번 찍었습니다.')
# #     if hit == 5:
# #         break # 반복문 종료

# coffee = 10
# while True :
#     print(f'남은 커피의 양은 {coffee}개 입니다.')
#     money = int(input("커피 한잔에 300원 입니다. 돈을 넣어 주세요 : "))
#     if money == 300 :
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300 :
#         print(f"거스름돈 {money-300}를 주고 커피를 줍니다.")
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")

#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

# for 반복문
# []는 파이썬 리스트 타입
for num in [1, 2, 3]:
    print (num)

for s in ['다람쥐', '코끼리', '펭귄', '기린', '아나콘다', '하마', '사슴']:
    print(s)

for c in '홍길동님' :
    print(c)


# for반복문과 자주쓰는 함수 range(시작, 끝) 리턴값은 시작~ 끝-1
for n in range(3):
    print(n)

# 1에서 100까지 합은
total = 0
for x in range(1,101):
    total += x

print("1에서 100까지 더한 값 : ", total)

#구구단 2단
for i in range(1,10):
    print(f'2 X {i} = {2*i}')


# 전체 구구단 출력 반복문을 중첩 이중반복문
for i in range(2,10):
    print()
    for j in range(1, 10) :
        print(f'{i}X{j} = {i*j}', end=" ")