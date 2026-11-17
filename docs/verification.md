# 검증 및 Git 실습 기록

## 프로그램 검증

다음 명령으로 자동 테스트를 실행할 수 있습니다.

```bash
python -m unittest discover -s tests -v
```

현재 검증 결과: `Ran 4 tests ... OK`

검증하는 내용은 다음과 같습니다.

- 정답과 오답 판정
- 기본 퀴즈 5개 이상 여부
- 잘못된 퀴즈 데이터 거부
- 문자, 빈 입력, 범위 밖 숫자 입력 후 재시도

수동 실행은 다음 명령으로 진행합니다.

```bash
python main.py
```

실행 확인 순서:

1. 이름 입력
2. `3`번으로 퀴즈 목록 확인
3. `4`번으로 최고 점수 확인
4. `5`번으로 종료

종료 시 `state.json`이 저장되고, 기존 파일이 있으면 `state.json.bak`으로 백업됩니다.

## JSON 보존 검증

`state.json`에는 `quizzes` 목록과 `best_score`가 저장됩니다. 프로그램을 종료한 뒤 다시 실행해도 같은 목록과 최고 점수를 불러오는지 확인합니다.

파일이 손상되면 기본 퀴즈로 시작합니다. 기존 정상 파일은 `state.json.bak`으로 남아 복구에 사용할 수 있습니다.

## Git 실습 기록

저장소에서 다음 명령으로 커밋과 브랜치 기록을 확인할 수 있습니다.

```bash
git log --oneline --decorate --graph --all
git branch -a
git status
```

이번 작업에서는 기능 단위로 작업한 뒤 `codyssey-final-completion` 브랜치를 `main`에 병합했습니다. 별도 복제 폴더에서 `git clone`을 수행하고 README를 수정해 push한 다음, 기존 폴더에서 `git pull`로 변경 사항을 가져왔습니다.

## 커밋 규칙

한 커밋에는 하나의 의미 있는 변경만 포함합니다.

```text
동사 + 변경 내용
```

예시:

- `Add persistent quiz questions`
- `Complete quiz game with classes and JSON persistence`
- `Document learning concepts and Git practice`

## 설계 설명

브랜치는 기능을 독립적으로 개발하고 문제가 생겼을 때 `main`에 영향을 줄이지 않기 위해 사용합니다. 병합(merge)은 검토가 끝난 기능을 완성본에 통합하는 작업입니다.

`Quiz`는 퀴즈 하나의 상태를 관리하고, `QuizGame`은 여러 퀴즈와 메뉴·저장을 관리합니다. 이렇게 나누면 문제 표현 방식과 게임 진행 방식을 각각 수정할 수 있어 재사용성이 높아집니다.

JSON은 사람이 읽기 쉽고 리스트와 객체를 함께 저장할 수 있다는 장점이 있습니다. 반면 데이터가 매우 커지면 전체 파일을 읽고 다시 써야 하므로 느려질 수 있으며, 그런 경우에는 SQLite나 데이터베이스를 고려할 수 있습니다.
