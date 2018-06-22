import random

print("베스킨라빈스 31 게임 프로그램입니다!")

while True:
    order = input('''순서를 입력하세요. (선공 1, 후공 0 입력) : ''')
    if order in ['0', '1']:
        order = int(order)
        break
    else:
        print("잘못된 입력입니다. 재입력해주세요.")

call = 0
count = 1

while call < 31:
    if count % 2 == order:
        # 사용자의 차례
        print('사용자의 차례')
        while True:
            size_of_call = input("호출할 개수를 입력하세요 : ")
            if size_of_call in ['1', '2', '3']:
                size_of_call = int(size_of_call)
                break
            else:
                print("잘못된 입력입니다. 재입력해주세요.")

        for _ in range(size_of_call):
            call += 1
            print("사용자 : '{0}'!!!".format(call))

            if call == 31:
                break

    else:
        # 컴퓨터의 차례
        print('컴퓨터의 차례')
        size_of_call = random.randint(1, 3)

        for _ in range(size_of_call):
            call += 1
            print("컴퓨터 : '{0}'!!!".format(call))

            if call == 31:
                break

    count += 1

if count % 2 == order:
    print("사용자의 승리!!")
else:
    print("컴퓨터의 승리!!")
