"""진입점: 간단한 CLI 채팅 루프.

실행:
    python -m src.main
"""
from .agent import SimpleAgent


def main() -> None:
    agent = SimpleAgent()
    print("Agent 시작 (종료: quit / exit)\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n종료합니다.")
            break

        if user_input.lower() in {"quit", "exit"}:
            print("종료합니다.")
            break
        if not user_input:
            continue

        answer = agent.run(user_input)
        print(f"Agent: {answer}\n")


if __name__ == "__main__":
    main()
