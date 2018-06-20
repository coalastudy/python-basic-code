print("학점계산기 프로그램입니다!")

subject_name = input("과목명을 입력해주세요 : ")
subject_score = input("당신의 점수를 입력해주세요 : ")
subject_grade = input("취득한 학점을 입력해주세요 : ")

calculating_way = input('''
학점 계산 방식을 선택해주세요.
1. 4.5 만점
2. 4.3 만점
''')

score = 0

if calculating_way == '1':
    if subject_score == 'A+':
        score = 4.5
    elif subject_score == 'A':
        score = 4.0
    elif subject_score == 'A-':
        score = "There is no value"
    elif subject_score == 'B+':
        score = 3.5
    elif subject_score == 'B':
        score = 3.0
    elif subject_score == 'B-':
        score = "There is no value"
    elif subject_score == 'C+':
        score = 2.5
    elif subject_score == 'C':
        score = 2.0
    elif subject_score == 'C-':
        score = "There is no value"
    elif subject_score == 'F':
        score = 0
    else:
        score = "There is no value"

    print('''
과목 이름 : {0}
당신의 점수 : {1}
변환한 점수 : {2}
당신의 취득학점 : {3}
'''.format(subject_name, subject_score, score, subject_grade))

elif calculating_way == '2':
    if subject_score == 'A+':
        score += 4.3
    elif subject_score == 'A':
        score += 4.0
    elif subject_score == 'A-':
        score += 3.7
    elif subject_score == 'B+':
        score += 3.3
    elif subject_score == 'B':
        score += 3.0
    elif subject_score == 'B-':
        score += 2.7
    elif subject_score == 'C+':
        score += 2.3
    elif subject_score == 'C':
        score += 2.0
    elif subject_score == 'C-':
        score += 1.7
    elif subject_score == 'F':
        score += 0
    else:
        score = "There is no value"

    print('''
과목 이름 : {0}
당신의 점수 : {1}
변환한 점수 : {2}
당신의 취득학점 : {3}
'''.format(subject_name, subject_score, score, subject_grade))

else:
    print("잘못된 연산 방법 입니다. 프로그램을 종료합니다.")