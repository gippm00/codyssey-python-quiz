# codyssey-python-quiz

Python으로 만든 콘솔 기반 객관식 퀴즈 게임입니다. Python 기초 문법과 Git 사용법을 연습하기 위해 제작했습니다.

## 퀴즈 주제와 선정 이유

주제는 Python 기초입니다. 이 과정에서 배운 `print`, 조건문, 자료형, 함수, 반복문을 퀴즈로 복습하고, 프로그램으로 직접 설명할 수 있도록 하기 위해 선택했습니다.

## 실행 방법

1. Python 3을 설치합니다.
2. 이 저장소를 내려받습니다.
3. 프로젝트 폴더에서 다음 명령을 실행합니다.

```bash
python main.py
```

## 기능 목록

- 객관식 퀴즈 풀기
- 정답·오답 채점 및 정답률 출력
- 새로운 퀴즈와 선택지 4개 등록
- 등록된 퀴즈 목록 확인
- 최고 점수 확인 및 갱신
- 퀴즈와 최고 점수의 JSON 파일 저장
- 잘못된 숫자, 빈 입력, 파일 오류 처리
- 저장 전 `state.json.bak` 자동 백업

## 파일 구조

```text
codyssey-python-quiz/
├── main.py       # Quiz와 QuizGame 클래스 및 실행 코드
├── state.json    # 퀴즈 목록과 최고 점수 저장 파일
├── README.md     # 프로젝트 설명서
├── docs/         # 실행 검증과 Git 실습 기록
├── tests/        # 입력 및 퀴즈 단위 테스트
└── .gitignore    # Git에서 제외할 파일 목록
```

## 데이터 파일 설명

`state.json`은 프로그램을 종료해도 데이터가 유지되도록 프로젝트 루트에 저장됩니다. UTF-8 인코딩을 사용하며 다음과 같은 구조를 가집니다.

```json
{
  "quizzes": [
    {
      "question": "문제 내용",
      "choices": ["선택지 1", "선택지 2", "선택지 3", "선택지 4"],
      "answer": 1
    }
  ],
  "best_score": 0
}
```

파일이 없으면 기본 퀴즈로 시작하고, 파일이 손상되었으면 안내 메시지를 출력한 뒤 기본 데이터로 복구합니다.

데이터를 저장할 때 기존 `state.json`은 `state.json.bak`으로 백업합니다. 저장 중 문제가 생기거나 이전 데이터가 필요하면 이 백업 파일을 사용해 복구할 수 있습니다. 데이터가 매우 커지면 전체 파일을 다시 저장해야 하므로 성능과 메모리 사용량이 증가할 수 있으며, 그런 경우에는 SQLite 같은 데이터베이스를 고려할 수 있습니다.

## 클래스 구조

- `Quiz`: 문제, 선택지, 정답을 보관하고 퀴즈를 출력하며 정답을 확인합니다.
- `QuizGame`: 메뉴, 게임 진행, 문제 추가, 목록 출력, 최고 점수, JSON 저장·불러오기를 관리합니다.

`Quiz`는 퀴즈 하나의 상태를 관리하고, `QuizGame`은 여러 퀴즈와 게임 흐름을 관리합니다. 클래스 기반 설계는 각 객체의 상태를 한 곳에서 관리하고, 기능을 메서드 단위로 재사용할 수 있다는 장점이 있습니다.

## 변경 시 참고할 메서드

- 문제 형식을 바꿀 때: `Quiz.__init__`, `Quiz.show`, `Quiz.from_dict`, `Quiz.to_dict`
- 입력 검증을 바꿀 때: `QuizGame.read_text`, `QuizGame.read_int`
- 저장 형식을 바꿀 때: `QuizGame.load_state`, `QuizGame.save_state`
- 메뉴 기능을 바꿀 때: `QuizGame.show_menu`, `QuizGame.run`

실행 검증과 Git 기록은 [`docs/verification.md`](docs/verification.md)에서 확인할 수 있으며, 자동 테스트는 다음 명령으로 실행합니다.

```bash
python -m unittest discover -s tests -v
```

## 학습한 내용

- `class`(클래스: 데이터와 기능을 묶은 설계도)로 프로그램 구조화
- `method`(메서드: 클래스 안에 정의한 함수)로 기능 분리
- `JSON`(데이터 저장 형식)과 `try/except`(예외 처리) 활용
- Git의 커밋, 브랜치, 병합, clone, pull 실습
