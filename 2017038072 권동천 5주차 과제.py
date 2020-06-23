def input_data () :
   print("%d번째 학생의 정보를 입력하세요.\n" % (value + 1))

   std_info[value]['학과'] = input("학생의 학과를 입력하세요 : ")
   std_info[value]['학번'] = input("학생의 학번을 입력하세요 : ")
   std_info[value]['이름'] = input("학생의 이름을 입력하세요 : ")
   std_info[value]['국어'] = int(input("학생의 국어 성적을 입력하세요.(0~100) : "))
   std_info[value]['영어'] = int(input("학생의 영어 성적을 입력하세요.(0~100) : "))
   std_info[value]['수학'] = int(input("학생의 수학 성적을 입력하세요.(0~100) : "))
   std_info[value]['총점'] = std_info[value]['국어'] + std_info[value]['영어'] +std_info[value]['수학']
   std_info[value]['평균'] = std_info[value]['총점'] / 3

def calc_Grade() :
    if (std_info[value]['평균'] >= 95) :
        std_info[value]['학점'] = 'A+'
    elif ((std_info[value]['평균'] < 95) and (std_info[value]['평균'] >= 90)) :
        std_info[value]['학점'] = 'A0'
    elif ((std_info[value]['평균'] < 90) and(std_info[value]['평균'] >= 85)) :
        std_info[value]['학점'] = 'B+'
    elif ((std_info[value]['평균'] < 85) and (std_info[value]['평균'] >= 80)) :
        std_info[value]['학점'] = 'B0'
    elif ((std_info[value]['평균'] < 80) and (std_info[value]['평균'] >= 75)) :
        std_info[value]['학점'] = 'C+'
    elif ((std_info[value]['평균'] < 75) and (std_info[value]['평균'] >= 70)) :
        std_info[value]['학점'] = 'C0'
    elif ((std_info[value]['평균'] < 70) and (std_info[value]['평균'] >= 65)) :
        std_info[value]['학점'] = 'D+'
    elif ((std_info[value]['평균'] < 65) and (std_info[value]['평균'] >= 60)) :
        std_info[value]['학점'] = 'D0'
    elif(std_info[value]['평균'] < 60) :
        std_info[value]['학점'] = 'F'

def search_NAME() :
    std_number = input("찾고 싶은 학생의 이름을 입력하세요 : ")
    for i in range (0, value + 1, 1) :
        if(std_number == std_info[i].get('이름')) :
            print(list(std_info[i].items()))
            break;

def del_info() :
    std_number = input("정보를 삭제하고 싶은 학생의 이름을 입력하세요 : ")
    for i in range(0, value + 1, 1) :
        if(std_number == std_info[i].get('이름')) :
            del(std_info[i])
            std_info.append({'학과':'', '학번':'', '이름':'','국어':'','영어':'','수학':'','총점':'','평균':'','학점':''})
            break

def sort_InfoList() :
    print("학번 순에 따라 정렬합니다. (오름차순) \n")
    std_info2 = sorted(std_info, key=itemgetter('학번'))
    for i in range(5-value, 5, 1) :
        print(list(std_info2[i].items()))

value = 0
i = 0
std_number = ''
std_info = [{'학과':'','학번':'','이름':'','국어':'','영어':'','수학':'','총점':'','평균':'','학점':''},
            {'학과':'','학번':'','이름':'','국어':'','영어':'','수학':'','총점':'','평균':'','학점':''},
            {'학과':'','학번':'','이름':'','국어':'','영어':'','수학':'','총점':'','평균':'','학점':''},
            {'학과':'','학번':'','이름':'','국어':'','영어':'','수학':'','총점':'','평균':'','학점':''},
            {'학과':'','학번':'','이름':'','국어':'','영어':'','수학':'','총점':'','평균':'','학점':''}]
std_info2 = [{}]

from operator import itemgetter

while (True) :
    print("1. 데이터 추가\n")
    print("2. 데이터 검색\n")
    print("3. 데이터 삭제\n")
    print("4. 데이터 정렬\n")
    print("0. 종료\n")

    number = int(input("번호를 입력하세요 : "))

    if number == 1 :
        input_data()
        calc_Grade()
        value += 1
    elif number == 2 :
        search_NAME()
    elif number == 3 :
        del_info()
        value -= 1
    elif number == 4 :
        sort_InfoList()
    elif number == 0 :
        print("프로그램을 종료합니다\n")
        break
