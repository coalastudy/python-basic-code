print("급여계산기 프로그램입니다!")

pay = input("시급을 입력해주세요 : ")
time_of_day = input("일일근무시간 : ")
day_of_month = input("한달근무일수 : ")

# 수습 적용 여부
practice = input('''
수습을 적용하나요?
1. 적용
2. 미적용
''')

pay = int(pay)
time_of_day = int(time_of_day)
day_of_month = int(day_of_month)

# 수습 변수 추가
practice = int(practice)

# 월급 계산
profit = pay * time_of_day * day_of_month

# 수습 적용
if practice == 1:
    practice_price = profit // 10
else:
    practice_price = 0

profit = profit - practice_price

# 결과 출력
print("예상 월급은 : {0}원입니다.\n\n".format(profit))
print("{0}원으로 무엇을 할 수 있을까요?".format(profit))
print("PC방 (1200원 기준) : {0}시간".format(profit // 1200))
print("점심 (7000원 기준) : {0}끼".format(profit // 7000))
print("영화 (11000원 기준) : {0}편".format(profit // 11000))
print("노래방 (20000원 기준) : {0}시간".format(profit // 20000))

print('''
열심히 일하시는 당신에게...
비록 세상이 그대를 속일지라도
슬퍼하거나 노여워하지 말아라
슬픈 날은 참고 견디라
기쁜 날이 오고야 말리니.''')