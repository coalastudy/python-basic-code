print("일반계산기 프로그램입니다!")

first = input("계산할 첫번째 값을 입력해주세요 : ")
second = input("계산할 두번째 값을 입력해주세요 : ")

first = int(first)
second = int(second)

# 결과 출력
print("\n\n두 개의 값 : {0} 와 {1}\n".format(first, second))
print("더하기 값 (a + b) : {0}".format(first + second))
print("빼기 값 (a - b) : {0}".format(first - second))
print("곱하기 값 (a * b) : {0}".format(first * second))
print("정수 나누기 값 (a // b) : {0}".format(first // second))
print("실수 나누기 값 (a / b) : {0}".format(first / second))
print("나머지 값 (a % b) : {0}".format(first % second))