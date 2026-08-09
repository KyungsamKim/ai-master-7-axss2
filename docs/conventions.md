# 협업 컨벤션

공용 레포에서 4명이 충돌 없이 작업하기 위한 최소 규칙입니다.

## 1. 폴더 규칙

- 모든 작업은 **본인 폴더** `members/{이름}/` 안에서만 합니다.
- 다른 사람 폴더, 루트 공통 파일(`README.md`, `.gitignore` 등)은 상의 없이 수정하지 않습니다.
- 폴더명은 **로마자 소문자**로 통일합니다. (예: `kyungsam`, `jihoon`) — 한글/대문자/공백 금지.

## 2. 브랜치 전략

사람별 폴더가 분리돼 있으므로 브랜치는 단순하게 갑니다.

- `main` : 항상 동작하는 기준 브랜치. **직접 push 금지.**
- 작업 브랜치: `feat/{이름}-{요약}` 형식
  - 예: `feat/kyungsam-rag-pipeline`, `fix/jihoon-prompt-bug`
- 작업 → PR → (가능하면 1명 이상 리뷰) → `main` 머지.

```bash
git switch -c feat/kyungsam-rag-pipeline
# ...작업...
git push -u origin feat/kyungsam-rag-pipeline
# GitHub에서 PR 생성
```

## 3. 커밋 메시지

`type: 요약` 형식을 권장합니다.

| type | 용도 |
|---|---|
| `feat` | 기능 추가 |
| `fix` | 버그 수정 |
| `docs` | 문서 |
| `refactor` | 리팩터링 |
| `chore` | 설정·잡일 |

예: `feat: add retriever with ChromaDB`

## 4. 의존성 관리

- **폴더별 독립 관리**가 원칙입니다. 각자 `requirements.txt`(또는 `pyproject.toml`)를 둡니다.
- 루트에 통합 의존성 파일을 만들지 않습니다. (버전 충돌 방지)
- 가상환경도 폴더별로 따로 만드세요.

## 5. 비밀 정보

- API 키, 토큰, `.env`는 **절대 커밋 금지**.
- 대신 `.env.example`에 키 이름만 적어 공유합니다.
- 실수로 커밋했다면 즉시 키를 폐기/재발급하세요. (히스토리에 남으면 삭제만으론 안전하지 않음)

## 6. shared/ 사용 여부

- 초기엔 만들지 않습니다. 정말 공유할 코드가 명확해질 때 논의 후 추가합니다.
- `shared/`는 4명이 동시에 건드리는 유일한 충돌 지점이 되기 쉬우므로, 넣기 전에 팀 합의를 거칩니다.
