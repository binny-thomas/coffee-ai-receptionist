from openai import OpenAI

from app.config import OPENAI_API_KEY
from app.config import OPENAI_MODEL


def get_client() -> OpenAI:
    """
    Create and return an authenticated OpenAI client.
    """

    if not OPENAI_API_KEY:
        raise ValueError(
            "OpenAI API key is missing. "
            "Please set OPENAI_API_KEY in your .env file."
        )

    return OpenAI(api_key=OPENAI_API_KEY)


def ask_ai(system_prompt: str, user_message: str) -> str:
    """
    Send a request to OpenAI and return the AI response.
    """

    client = get_client()

    response = client.responses.create(
        model=OPENAI_MODEL,
        instructions=system_prompt,
        input=user_message,
    )

    return response.output_text