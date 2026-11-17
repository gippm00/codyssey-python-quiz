import json
import shutil
from pathlib import Path


class Quiz:
    """하나의 객관식 퀴즈를 표현하는 클래스입니다."""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

    @classmethod
    def from_dict(cls, data):
        question = data["question"]
        choices = data["choices"]
        answer = data["answer"]
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제가 올바르지 않습니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개여야 합니다.")
        if not all(isinstance(choice, str) and choice.strip() for choice in choices):
            raise ValueError("선택지 내용이 올바르지 않습니다.")
        if not isinstance(answer, int) or not 1 <= answer <= 4:
            raise ValueError("정답은 1부터 4 사이여야 합니다.")
        return cls(question.strip(), [choice.strip() for choice in choices], answer)


class QuizGame:
    """퀴즈 목록, 게임 진행, 파일 저장을 관리하는 클래스입니다."""

    STATE_FILE = Path(__file__).resolve().parent / "state.json"
    BACKUP_FILE = Path(__file__).resolve().parent / "state.json.bak"

    def __init__(self):
        self.quizzes = self.default_quizzes()
        self.best_score = 0
        self.load_state()

    @staticmethod
    def default_quizzes():
        return [
            Quiz("Python에서 화면에 글자를 출력하는 함수는 무엇일까요?", ["input", "print", "open", "len"], 2),
            Quiz("Python에서 조건을 표현할 때 사용하는 키워드는 무엇일까요?", ["if", "for", "def", "class"], 1),
            Quiz("Python에서 여러 값을 순서대로 저장하는 자료형은 무엇일까요?", ["list", "bool", "int", "str"], 1),
            Quiz("문자열을 정수로 바꾸는 함수는 무엇일까요?", ["str", "bool", "int", "list"], 3),
            Quiz("반복문을 끝내는 데 사용하는 키워드는 무엇일까요?", ["continue", "stop", "break", "return"], 3),
        ]

    def load_state(self):
        if not self.STATE_FILE.exists():
            return
        try:
            with self.STATE_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
            loaded_quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            if not loaded_quizzes:
                raise ValueError("퀴즈가 없습니다.")
            best_score = data.get("best_score", 0)
            if not isinstance(best_score, int) or best_score < 0:
                raise ValueError("최고 점수가 올바르지 않습니다.")
            self.quizzes = loaded_quizzes
            self.best_score = best_score
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("state.json을 읽을 수 없어 기본 퀴즈 데이터로 시작합니다.")
            self.quizzes = self.default_quizzes()
            self.best_score = 0

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            if self.STATE_FILE.exists():
                shutil.copyfile(self.STATE_FILE, self.BACKUP_FILE)
            with self.STATE_FILE.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"저장 완료: {self.STATE_FILE.name}")
        except OSError:
            print("state.json을 저장하지 못했습니다.")

    @staticmethod
    def read_text(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("빈 입력은 사용할 수 없습니다. 다시 입력해주세요.")

    @staticmethod
    def read_int(prompt, minimum, maximum):
        while True:
            value = input(prompt).strip()
            if not value:
                print("빈 입력은 사용할 수 없습니다.")
                continue
            try:
                number = int(value)
            except ValueError:
                print("숫자를 입력해주세요.")
                continue
            if not minimum <= number <= maximum:
                print(f"{minimum}부터 {maximum} 사이의 숫자를 입력해주세요.")
                continue
            return number

    def show_menu(self):
        print("\n====== 퀴즈 게임 메뉴 ======")
        print("1. 퀴즈 풀기")
        print("2. 문제 추가하기")
        print("3. 문제 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 종료")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        score = 0
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n문제 {number}/{len(self.quizzes)}")
            quiz.show()
            user_answer = self.read_int("정답 번호를 입력하세요: ", 1, 4)
            if quiz.is_correct(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")
        print(f"\n최종 점수: {score}/{len(self.quizzes)}")
        accuracy = score / len(self.quizzes) * 100
        print(f"정답률: {accuracy:.1f}%")
        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
        print(f"최고 점수: {self.best_score}/{len(self.quizzes)}")
        self.save_state()

    def add_quiz(self):
        print("\n새로운 문제를 추가합니다.")
        question = self.read_text("문제를 입력하세요: ")
        choices = []
        for number in range(1, 5):
            choices.append(self.read_text(f"{number}번 선택지를 입력하세요: "))
        answer = self.read_int("정답 번호를 입력하세요(1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("문제가 추가되고 state.json에 저장되었습니다.")

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print("\n====== 등록된 퀴즈 목록 ======")
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")
            for choice_number, choice in enumerate(quiz.choices, start=1):
                print(f"   {choice_number}) {choice}")

    def run(self):
        print("퀴즈 게임을 시작합니다!")
        player = self.read_text("플레이어의 이름을 입력하세요: ")
        print(f"{player}님, 환영합니다!")
        while True:
            self.show_menu()
            menu_choice = self.read_int("원하는 메뉴 번호를 입력하세요: ", 1, 5)
            if menu_choice == 1:
                self.play_quiz()
            elif menu_choice == 2:
                self.add_quiz()
            elif menu_choice == 3:
                self.list_quizzes()
            elif menu_choice == 4:
                print(f"최고 점수: {self.best_score}/{len(self.quizzes)}")
            else:
                print("퀴즈 게임을 종료합니다.")
                self.save_state()
                break


def main():
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되었습니다. 현재 데이터를 저장하고 안전하게 종료합니다.")
        game.save_state()


if __name__ == "__main__":
    main()
