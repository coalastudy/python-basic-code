import random

print("야구 게임 프로그램입니다!")

# 랜덤하게 4자리의 숫자 만들기 (각 자리의 수는 중복 불가)
answer = list()

while len(answer) != 4:
    new_number = random.randint(0, 9)
    if new_number not in answer:
        answer.append(new_number)

print(answer)

# 유저에게 입력 받음
your_answer = input("답을 맞추어 보세요 : ")

print(your_answer)