print("퀴즈 게임을 시작합니다!")
player = input("플레이어의 이름을 입력하세요")
print(player + "님, 환영합니다!")
print(type(player))

print(type(int("123")))
answer = int(input("정답을 입력하세요: "))
print(answer == 2)
score = 10
if answer == 2:
    print("정답입니다!")
    score = 10
    score += 10
else:
    print("오답입니다!")
    score = 0
print("현재 점수: ", score) 

for i in range(1, 4):
    print("문제 번호: ", i) 
    user_answer = int(input("정답을 입력하세요: "))
    print("입력한 정답: ", user_answer)