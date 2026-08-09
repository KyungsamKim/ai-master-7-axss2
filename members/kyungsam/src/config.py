"""설정 로드 모듈.

.env 파일에서 환경 변수를 읽어옵니다.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "claude-sonnet-4-5")

    @classmethod
    def validate(cls) -> None:
        if not cls.ANTHROPIC_API_KEY:
            raise RuntimeError(
                "ANTHROPIC_API_KEY 가 설정되지 않았습니다. "
                ".env.example 을 복사해 .env 를 만들고 키를 채워주세요."
            )


config = Config()
