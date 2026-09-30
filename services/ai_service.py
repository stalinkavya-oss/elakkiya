from openai import OpenAI

from ..config import settings


def generate_ai_response(message: str) -> str:
    """
    Send the user's message to the configured LLM
    and return the generated response.
    """

    if not settings.openai_api_key:
        return (
            "AI service is not configured yet. "
            "Please add your OPENAI_API_KEY to the .env file."
        )

    try:
        client = OpenAI(api_key=settings.openai_api_key)

        response = client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are PocketSmart AI, a helpful personal "
                        "finance assistant. Give clear, simple and "
                        "practical answers."
                    ),
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content or (
            "Sorry, I could not generate a response."
        )

    except Exception as exc:
        return f"AI service error: {exc}"