print("급여계산기 프로그램입니다!")

pay = 7000
time_of_day = 8
day_of_month = 19

# 월급 계산
profit = pay * time_of_day * day_of_month

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