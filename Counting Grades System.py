# 등급을 구하는 함수
def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


# 평균과 등급을 리스트에 추가하는 함수
def appending(grade_lst):
    for i in range(len(grade_lst)):
        avg = (int(grade_lst[i][2]) + int(grade_lst[i][3]))/2
        grade_lst[i].append(avg)
        grade_lst[i].append(get_grade(avg))
    return grade_lst


# 평균 기준 내림차순으로 만들어주는 함수 생성
def descending():
    global grade_lst   # 사용하고자 하는 변수 global 함수 안에서 선언해주기
    sorted_grade_lst = sorted(grade_lst, key=lambda x: x[4], reverse=True)
    grade_lst = sorted_grade_lst


# 명령어 함수
# [전체 학생 정보 출력] 학생 전체 목록을 평균 점수를 기준으로 내림차순으로 출력
def show():
    global grade_lst
    descending()

    label = "Student ID\t\tStudent Name\t\tMidterm\t\tFinal\t\tAverage\t\tGrade\n-------------------------------------------------------------------------------------"
    print(label)
    for stu in grade_lst:
        # print(stu)
        stu_id = stu[0]
        stu_name = stu[1]
        mid_score = stu[2]
        final_score = stu[3]
        avg = stu[4]
        grade = stu[5]
        print("%10s %17s %12s %12s %12s %8s" %(stu_id, stu_name, mid_score, final_score, avg, grade))


# [특정 학생 정보 출력] 사용자가 원하는 특정 학생 정보 평균 점수를 기준으로 내림차순으로 출력
def show_student(ans):
    label = "Student ID\t\tStudent Name\t\tMidterm\t\tFinal\t\tAverage\t\tGrade\n-------------------------------------------------------------------------------------"
    print(label)
    #print(stu)
    stu_id = ans[0]
    stu_name = ans[1]
    mid_score = ans[2]
    final_score = ans[3]
    avg = ans[4]
    grade = ans[5]
    print("%10s %17s %12s %12s %12s %8s" %(stu_id, stu_name, mid_score, final_score, avg, grade))


# [특정 학생 검색] 학번 입력 ---> 학번, 이름, 중간, 기말, 평균, 학점 출력
def search(student_id):
    for i in range(0, len(grade_lst)):
        if student_id == grade_lst[i][0]:
            ans = grade_lst[i]
            answ = show_student(ans)
            return answ
        else:
            pass
    print('NO SUCH PERSON.')


# [점수 수정] 학번 입력 ---> 중간고사인지 기말고사인지 ---> 새로운 점수 입력과 등급 수정 같이 하기
def change_score(student_id):
    stu_lst = []
    for i in range(0, len(grade_lst)):
        stu_lst.append(grade_lst[i][0])
    if student_id in stu_lst:
        which_test = input('Mid/Final?:')
        if which_test == 'mid':
            new_mid_score = input('Input new score:')
            for i in range(len(stu_lst)):
                if stu_lst[i] == student_id:
                    grade_lst[i][2] = new_mid_score
                    grade_lst[i][4] = (int(grade_lst[i][2]) + int(grade_lst[i][3])) / 2
                    grade_lst[i][5] = get_grade(grade_lst[i][4])
                    ans = grade_lst[i]
                    answ = show_student(ans)
                    print(answ)


        elif which_test == 'final':
            new_final_score = input('Input new score:')
            for i in  range(len(stu_lst)):
                if stu_lst[i] == student_id:
                    grade_lst[i][3] = new_final_score
                    grade_lst[i][4] = (int(grade_lst[i][2]) + int(grade_lst[i][3])) / 2
                    grade_lst[i][5] = get_grade(grade_lst[i][4])
                    ans = grade_lst[i]
                    answ = show_student(ans)
                    print(answ)
    else:
        print('NO SUCH PERSON.')


# [학생 추가] 학번, 이름, 중간, 기말 점수 입력 ---> 평균과 등급 추가하기(appending_data 함수) ---> 이후 show 함수 사용하면 전체 리스트 출력
def add(student_id):
    id_lst = []
    new_lst = []
    for i in range(0, len(grade_lst)):
        id_lst.append(grade_lst[i][0])
    if student_id in id_lst:
        print('ALREADY EXISTS.')
    else:
        new_lst.append(student_id)
        name = input('Name:')
        new_lst.append(name)
        new_mid_score = input('Midterm Score:')
        new_lst.append(new_mid_score)
        new_final_score = input('Final Score:')
        new_lst.append(new_final_score)

        average2 = (int(new_lst[2]) + int(new_lst[3])) / 2
        new_lst.append(average2)
        grade2 = get_grade(average2)
        new_lst.append(grade2)
        grade_lst.append(new_lst)
        print('Student added.')


# [등급 검색] 특정 등급 입력 ---> 그 등급에 해당하는 학생 모두 출력
def search_grade(student_grade):
    if student_grade == 'A':
        for i in range(0, len(grade_lst)):
            if grade_lst[i][5] == 'A':
                ans = grade_lst[i]
                show_student(ans)

        if len(grade_lst[i]) == 0:
            print('NO RESULTS.')

    elif student_grade == 'B':
        for i in range(0, len(grade_lst)):
            if grade_lst[i][5] == 'B':
                ans = grade_lst[i]
                show_student(ans)

        if len(grade_lst[i]) == 0:
            print('NO RESULTS.')


    elif student_grade == 'C':
        for i in range(0, len(grade_lst)):
            if grade_lst[i][5] == 'C':
                ans = grade_lst[i]
                show_student(ans)

        if len(grade_lst[i]) == 0:
            print('NO RESULTS.')

    elif student_grade == 'D':
        for i in range(0, len(grade_lst)):
            if grade_lst[i][5] == 'D':
                ans = grade_lst[i]
                show_student(ans)

        if len(grade_lst[i]) == 0:
            print('NO RESULTS.')

    elif student_grade == 'F':
        for i in range(0, len(grade_lst)):
            if grade_lst[i][5] == 'F':
                ans = grade_lst[i]
                show_student(ans)

        if len(grade_lst[i]) == 0:
            print('NO RESULTS.')


# [특정 학생 삭제] 삭제하고자 하는 학번 입력 ---> 삭제하고 'Student removed' 출력
def remove(student_id):
    stu_lst = []
    for i in range(0, len(grade_lst)):
        stu_lst.append(grade_lst[i][0])
    if len(stu_lst) == 0:
        print('List is empty.')
    if student_id in stu_lst:
        for i in range(0, len(grade_lst)):
            if student_id != grade_lst[i][0]:
                continue
            else:
                del grade_lst[i]
                print('Student removed')
                return grade_lst
    else:
        print('NO SUCH PERSON.')



# [프로그램 종료] 편집할 내용 저장 여부 묻기 ---> 저장 선택 시 파일명 입력받기 ---> 저장(저장 시 목록의 순서는 평균 기준 내림차순????)
def quit(grade_lst):
    question_mark = input('Save data? [yes/no]').lower()
    if question_mark == 'yes':
        put_filename = input('File name:')

        fw = open(put_filename, 'a')
        for stu in grade_lst:
            write_line = "%s\t%s\t%s\t%s\n" % (stu[0], stu[1], stu[2], stu[3])
            fw.write(write_line)

        fw.close()

# 프로그램 시작
grade_lst = []

# 파일을 라인 단위로 불러오기, 데이터 리스트로 가져와서 저장하기
filename = 'students.txt'

with open(filename, 'r') as data:
    for i in data:
        i = i.replace('\t', ' ').replace('\n', '').split() # replace 두번 중복 사용 가능함
        grade_lst.append(i)
    for j in range(len(grade_lst)):
        # grade_lst[j][0] = int(grade_lst[j][0])
        grade_lst[j][1] += ' ' + grade_lst[j][2]
        del grade_lst[j][2]


#print(grade_lst) # 초기화 테스트 :
###

appending(grade_lst)
##print(grade_lst) # 평균, 학점 초기화 :

# 명령어 입력받기
user_command = input('#').lower()

# 함수 실행 파트
while user_command != 'quit':
    valid_command = ('show', 'search', 'changescore', 'searchgrade', 'add', 'remove', 'quit')
    if user_command in valid_command:
        if user_command == 'show':
            #grade_lst = show() # 오류발생 : show()에서 리턴해주는게 없음 > show()의 리턴값은 None > grade_lst에 none값이 대입된것.
            show()
            #print("test: ", grade_lst)

        elif user_command == 'search':
            student_id = input('Student ID:')
            search(student_id)

        elif user_command == 'changescore':
            student_id = input('Student ID:')
            change_score(student_id)

        elif user_command == 'searchgrade':
            student_grade = input('Grade to search:')
            search_grade(student_grade)

        elif user_command == 'add':
            student_id = input('Student ID:') # 입력 받기
            add(student_id) # add 함수 실행

        elif user_command == 'remove':
            student_id = input('Student ID:')
            remove(student_id)

    user_command = input('#').lower()  # 초기화

quit(grade_lst)

data.close()