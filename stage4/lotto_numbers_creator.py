import random

print("로또 번호 생성기 프로그램입니다!")

lotto_numbers = list()

while True:
    new_number = random.randrange(1, 46)
    if new_number not in lotto_numbers:
        lotto_numbers.append(random.randrange(1, 46))

    if len(lotto_numbers) == 7:
        break

# print('''
# 랜덤 로또 발생기 입니다.
# 당첨 번호 : {0}, {1}, {2}, {3}, {4}, {5}
# 2등 보너스 볼 : {6}
# '''.format(lotto_numbers[0],
#            lotto_numbers[1],
#            lotto_numbers[2],
#            lotto_numbers[3],
#            lotto_numbers[4],
#            lotto_numbers[5],
#            lotto_numbers[6]))

print("랜덤 로또 발생기 입니다.")
print("당첨 번호 : ", end="")

for index, value in enumerate(lotto_numbers):
    if index == len(lotto_numbers)-1:
        print("\n2등 보너스볼 : {0}".format(value))
    else:
        print(value, end=' ')
