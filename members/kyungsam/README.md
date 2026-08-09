# {주제명} — Kyungsam

> 이 폴더는 개인 작업 공간입니다. 아래 내용을 본인 주제에 맞게 채워주세요.

## 주제 개요

한 줄 요약: (예) 사내 문서를 검색해 답변하는 RAG 기반 Q&A Agent

- **문제 정의**:
- **접근 방식**:
- **핵심 기술**: LangGraph / LangChain / ChromaDB / ...

## 아키텍처

```
사용자 입력 → [라우팅] → [Retriever] → [LLM] → 응답
```
(간단한 다이어그램이나 설명을 넣어주세요.)

## 폴더 구조

```
kyungsam/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── main.py          # 진입점 (CLI 실행)
│   ├── agent.py         # Agent 정의
│   └── config.py        # 설정 로드
└── notebooks/           # 실험용 (선택)
```

## 실행 방법

```bash
cd members/kyungsam
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env               # 키 입력
python -m src.main                 # 또는: python src/main.py
```

## 환경 변수

`.env.example` 참고. 최소한 아래가 필요합니다.

- `ANTHROPIC_API_KEY` : Claude API 키

## 진행 메모

- [ ] 주제 확정
- [ ] 프로토타입
- [ ] Agent 완성
- [ ] 데모 / 발표 준비
