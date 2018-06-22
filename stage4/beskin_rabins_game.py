import random

print("베스킨라빈스 31 게임 프로그램입니다!")

# 순서 입력
order = input("먼저하시겠습니까? (y or n)")

user_order = 1
if order is 'y':
    user_order = 1
elif order is 'n':
    user_order = 0

current = 0
is_end = False

# 게임 시작
for count in range(1, 32):

    # 유저 차례
    if count%2 is user_order:
        user_call = input("몇 개를 입력할까요?")

        for _ in range(int(user_call)):
            current = current + 1
            print("유저 호출 : " + str(current))

            if current is 31 :
                print("컴퓨터 승리!!!!!")
                is_end = True
                break

    # 컴퓨터 차례
    else:
        computer_call = random.randrange(1, 4)

        for _ in range(int(computer_call)):
            current = current + 1
            print("컴퓨터 호출 : " + str(current))

            if current is 31:
                print("유저 승리!!!!!")
                is_end = True
                break

    if is_end:
        break
