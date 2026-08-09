# AI Master 7기 — AX Solution 서비스2팀

AI Master 7기 과제 공용 레포지토리입니다. 팀원 각자가 주제를 정해 독립적으로 AI Agent를 개발합니다.

## 과제 개요

- **과정**: AI Master 7기
- **팀**: AX Solution 서비스2팀
- **형태**: 팀원별 개별 주제 → 각자 Agent 개발
- **작업 원칙**: 각자 `members/{이름}/` 폴더 안에서만 작업 (충돌 방지)

## 팀원 & 주제

| 이름 | 폴더 | 주제 | 상태 |
|---|---|---|---|
| Kyungsam | [`members/kyungsam`](members/kyungsam) | (주제 작성) | 🚧 진행중 |
| (이름) | [`members/member-2`](members/member-2) | (주제 작성) | ⬜ 예정 |
| (이름) | [`members/member-3`](members/member-3) | (주제 작성) | ⬜ 예정 |
| (이름) | [`members/member-4`](members/member-4) | (주제 작성) | ⬜ 예정 |

> 폴더명 `member-2 ~ 4`는 임시입니다. 각자 로마자 이름으로 바꿔주세요 (예: `jihoon`, `minsu`).

## 저장소 구조

```
ai-master-7-axss2/
├── README.md            # 이 파일
├── .gitignore           # 공통 무시 규칙
├── .github/             # PR 템플릿 등
├── docs/                # 공용 문서 (컨벤션, 아키텍처 가이드)
├── members/             # 팀원별 작업 공간 (독립)
│   ├── kyungsam/
│   ├── member-2/
│   ├── member-3/
│   └── member-4/
└── shared/              # (필요 시) 공통 유틸·프롬프트 — 초기엔 비워둠
```

## 시작하기

1. 레포를 클론합니다.
2. **본인 폴더로 이동**해서 작업합니다. `cd members/{본인이름}`
3. 각 폴더는 독립된 의존성을 가집니다. 폴더별로 가상환경을 따로 만드세요.
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. 작업 규칙은 [`docs/conventions.md`](docs/conventions.md)를 먼저 읽어주세요.

## 규칙 요약

- 본인 폴더 밖(다른 사람 폴더, 루트 공통 파일)은 함부로 수정하지 않습니다.
- `main` 직접 push 금지. 브랜치 → PR → 리뷰 후 머지.
- `.env`, API 키 등 비밀 정보는 커밋하지 않습니다. (`.env.example`만 공유)
