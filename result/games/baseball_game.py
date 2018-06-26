import random

def play_game():
    print("야구 게임 프로그램입니다!")

    # 랜덤하게 4자리의 숫자 만들기 (각 자리의 수는 중복 불가)
    answer = list()

    while len(answer) != 4:
        new_number = random.randint(0, 9)
        if new_number not in answer:
            answer.append(new_number)

    # print(answer)

    strike = 0
    count = 0

    while strike != 4:
        # 유저에게 입력 받음
        your_answer = input("답을 맞추어 보세요 : ")

        count += 1
        strike = 0
        ball = 0

        # 스트라이크, 볼 검사
        for index, value in enumerate(your_answer):
            # print("index : {0}, value : {1}".format(index, value))
            if int(value) == answer[index]:
                strike += 1
            elif int(value) in answer:
                ball += 1

        if strike == 0 and ball == 0:
            print("Out!!!!!!!!!!!")
        else:
            print("{0} 스트라이크 {1} 볼입니다.".format(strike, ball))

    print("{0}번만에 정답을 맞추셨습니다!".format(count))