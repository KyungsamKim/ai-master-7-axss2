"""가장 단순한 형태의 Agent 샘플.

여기서는 도구 없이 LLM 호출만 하는 뼈대를 제공합니다.
본인 주제에 맞게 LangGraph 노드/툴/RAG 등을 붙여 확장하세요.
"""
from anthropic import Anthropic

from .config import config


class SimpleAgent:
    """LLM 한 번 호출하는 최소 Agent 예시."""

    def __init__(self) -> None:
        config.validate()
        self.client = Anthropic(api_key=config.ANTHROPIC_API_KEY)
        self.model = config.MODEL_NAME

    def run(self, user_input: str) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system="당신은 사용자를 돕는 한국어 AI 어시스턴트입니다.",
            messages=[{"role": "user", "content": user_input}],
        )
        # content 블록 중 텍스트만 합쳐서 반환
        return "".join(
            block.text for block in message.content if block.type == "text"
        )


# --- LangGraph 로 확장할 때의 골격 (참고용, 주석) ---
#
# from langgraph.graph import StateGraph, END
# from typing import TypedDict
#
# class AgentState(TypedDict):
#     input: str
#     output: str
#
# def call_model(state: AgentState) -> AgentState:
#     ...
#
# graph = StateGraph(AgentState)
# graph.add_node("model", call_model)
# graph.set_entry_point("model")
# graph.add_edge("model", END)
# app = graph.compile()
