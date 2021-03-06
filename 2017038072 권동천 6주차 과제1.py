from operator import itemgetter

class Std_Info :
    value = 0
    std_info = []
    std_number = ''
    std_info2 = [{}]
    # 데이터 입력 함수
    def input_data (self) :
        print("%d번째 학생의 정보를 입력하세요.\n" % (self.value + 1))

        self.std_info[self.value]['학과'] = input("학생의 학과를 입력하세요 : ")
        self.std_info[self.value]['학번'] = input("학생의 학번을 입력하세요 : ")
        self.std_info[self.value]['이름'] = input("학생의 이름을 입력하세요 : ")
        self.std_info[self.value]['국어'] = int(input("학생의 국어 성적을 입력하세요.(0~100) : "))
        self.std_info[self.value]['영어'] = int(input("학생의 영어 성적을 입력하세요.(0~100) : "))
        self.std_info[self.value]['수학'] = int(input("학생의 수학 성적을 입력하세요.(0~100) : "))
        self.std_info[self.value]['총점'] = self.std_info[self.value]['국어'] + self.std_info[self.value]['영어'] +self.std_info[self.value]['수학']
        self.std_info[self.value]['평균'] = self.std_info[self.value]['총점'] / 3
    # 평균을 받아서 학점을 계산하는 함수
    def calc_Grade(self) :
        if (self.std_info[self.value]['평균'] >= 95) :
            self.std_info[self.value]['학점'] = 'A+'
        elif ((self.std_info[self.value]['평균'] < 95) and (self.std_info[self.value]['평균'] >= 90)) :
            self.std_info[self.value]['학점'] = 'A0'
        elif ((self.std_info[self.value]['평균'] < 90) and(self.std_info[self.value]['평균'] >= 85)) :
            self.std_info[self.value]['학점'] = 'B+'
        elif ((self.std_info[self.value]['평균'] < 85) and (self.std_info[self.value]['평균'] >= 80)) :
            self.std_info[self.value]['학점'] = 'B0'
        elif ((self.std_info[self.value]['평균'] < 80) and (self.std_info[self.value]['평균'] >= 75)) :
            self.std_info[self.value]['학점'] = 'C+'
        elif ((self.std_info[self.value]['평균'] < 75) and (self.std_info[self.value]['평균'] >= 70)) :
            self.std_info[self.value]['학점'] = 'C0'
        elif ((self.std_info[self.value]['평균'] < 70) and (self.std_info[self.value]['평균'] >= 65)) :
            self.std_info[self.value]['학점'] = 'D+'
        elif ((self.std_info[self.value]['평균'] < 65) and (self.std_info[self.value]['평균'] >= 60)) :
            self.std_info[self.value]['학점'] = 'D0'
        elif(self.std_info[self.value]['평균'] < 60) :
            self.std_info[self.value]['학점'] = 'F'
    # 학생을 찾을 때, 이름을 검색하여 찾을 함수
    def search_NAME(self, i) :
        self.std_number = input("찾고 싶은 학생의 이름을 입력하세요 : ")
        for i in range (0, self.value + 1, 1) :
            if(self.std_number == self.std_info[i].get('이름')) :
                print(list(self.std_info[i].items()))
                break
    # 학생의 정보를 삭제할때, 이름을 검색하여 삭제하는 함수
    def del_info(self, i) :
        self.std_number = input("정보를 삭제하고 싶은 학생의 이름을 입력하세요 : ")
        for i in range(0, self.value + 1, 1) :
            if(self.std_number == self.std_info[i].get('이름')) :
                del(self.std_info[i])
                break
    # 학생들의 정보를 정렬하여 출력하는 함수
    def sort_InfoList(self, i) :
        print("학번 순에 따라 정렬합니다. (오름차순) \n")
        self.std_info2 = sorted(self.std_info, key=itemgetter('학번'))
        for i in range(0, self.value, 1) :
            print(list(self.std_info2[i].items()))

StudentInfo = Std_Info()
i = 0
while (True) :
    print("1. 데이터 추가\n")
    print("2. 데이터 검색\n")
    print("3. 데이터 삭제\n")
    print("4. 데이터 정렬\n")
    print("0. 종료\n")

    number = int(input("번호를 입력하세요 : "))

    if number == 1 :
        StudentInfo.std_info.append({'학과':'','학번':'','이름':'','국어':'','영어':'','수학':'','총점':'','평균':'','학점':''})
        StudentInfo.input_data()
        StudentInfo.calc_Grade()
        StudentInfo.value += 1
    elif number == 2 :
        StudentInfo.search_NAME(i)
    elif number == 3 :
        StudentInfo.del_info(i)
        StudentInfo.value -= 1
    elif number == 4 :
        StudentInfo.sort_InfoList(i)
    elif number == 0 :
        print("프로그램을 종료합니다\n")
        break
