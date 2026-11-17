print("퀴즈 게임을 시작합니다!")
player = input("플레이어의 이름을 입력하세요:")
print(player + "님, 환영합니다!")
print("====== 퀴즈 게임 메뉴 ======")

score = 0
wrong_count = 0
high_score = 0
try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read()) # high_score.txt 파일을 읽어와서 정수로 변환하여 high_score 변수에 저장
except FileNotFoundError: # high_score.txt 파일이 없으면
    high_score = 0 # high_score 변수에 0을 저장
questions = [
    "1 + 1은 얼마일까요?",
    "3 + 2는 얼마일까요?",
    "5 - 3은 얼마일까요?",
    "4 × 2는 얼마일까요?",
    "10 - 4는 얼마일까요?"
]
answers = [2, 5, 2, 8, 6]
try:
    with open("questions.txt", "r") as file:
        lines = file.readlines() # questions.txt 파일내용을 한줄씩 나눠서, lines 리스트에 저장
        for i in range(0, len(lines), 2): # 0부터 lines 리스트의 길이까지 2씩 증가하며 반복
            questions.append(lines[i].strip())    
            answers.append(int(lines[i + 1].strip()))
except FileNotFoundError: # questions.txt 파일이 없으면
    pass # 아무것도 하지 않음
         
while True : # 참인동안 반복
    print("1. 퀴즈 풀기")
    print("2. 문제 추가하기")
    print("3. 문제 목록 보기")
    print("4. 최고 점수 확인")
    print("5. 종료") 
    menu_choice = input("원하는 메뉴 번호를 입력하세요: ") #사용자가 원하는 메뉴 번호를 입력받아(함수) menu_choice(변수)에 저장
    if menu_choice == "1":
        score = 0  # 점수 초기화
        wrong_count = 0
        for i in range(1, len(questions) + 1): # 1부터 문제 개수까지 차례로 i에 넣으며 반복 
            print("문제 번호: ", i) #문제번호 i 출력 
            print(questions[i - 1]) #질문리스트의 
            while True: # 참이면 반복
                try: # 입력값이 정수인지 확인
                    user_answer = int(input("정답을 입력하세요: ")) # 사용자 입력값 받기. "정답을 입력하세요: " 출력하고 사용자가 입력한 값을 정수로 변환하여 user_answer에 저장
                    break # 멈춤
                except ValueError: # 에러가 안나면 건너뛰고, 에러가 나면 아래 코드 실행
                    print("정수를 입력해주세요.") # 정수를 입력하라는 안내문 출력
                    continue # 반복 
        
            print("입력한 정답: ", user_answer) # 사용자가 입력한 정답 출력
            if user_answer == answers[i - 1]:   # 사용자가 입력한 정답이 정답리스트의 i-1번째 값과 같으면
                print("정답입니다!") # "정답입니다!" 출력
                score += 1
            else:
                print("오답입니다!")
                wrong_count += 1
        print("최종 점수:", score)
        if score > high_score:
            high_score = score
            with open("high_score.txt", "w") as file:
                file.write(str(high_score)) # file에 high_score를 문자열로 변환하여 저장

    
        print("틀린 문제 수:", wrong_count)
        total_questions = len(questions)
        accuracy = score / total_questions * 100

        print("정답률:", round(accuracy, 1))    
        if not (score == total_questions):
            print("만점이 아닙니다!")
        else:
            print("만점입니다!")

    elif menu_choice == "2":
        print("새로운 문제를 추가합니다.")
        new_question = input("추가할 문제를 입력하세요: ")
        questions.append(new_question) #questions 리스트에 append() 함수를 실행해. 이때 넘겨줄 값은 new_question(변수)로, 사용자가 입력한 새로운 문제를 questions 리스트에 추가
        try:
            new_answer = int(input("새로운 문제의 정답을 입력하세요: "))
        except ValueError:
            print("정수를 입력해주세요.")
            continue
        answers.append(new_answer)
        print("문제가 추가 되었습니다!")
        try:
            with open("questions.txt", "a") as file:
                file.write(new_question + "\n") # file에 new_question을 문자열로 변환하여 저장
                file.write(str(new_answer) + "\n")
        except FileNotFoundError:
                    pass

    
    elif menu_choice == "3":
        print("문제 목록을 보여드립니다.")
        for number, question in enumerate(questions, start=1):#enumerate() 함수를 사용하여 questions 리스트의 각 문제와 그에 해당하는 번호를 가져옴. start=1로 설정하여 번호가 1부터 시작하도록 함
            print(number, ".", question) # 번호, 점, 문제 내용 출력

    elif menu_choice == "4":
        print("최고 점수:", high_score)

    elif menu_choice == "5": # 앞의 조건들이 아니고, 사용자가 5번 메뉴를 선택하면
        print("퀴즈 게임을 종료합니다.")
        break # 반복문 종료
    else: # 앞의 조건들이 아니고, 사용자가 1번과 5번 메뉴를 선택하지 않으면
        print("아직 사용할 수 없는 메뉴입니다.")



