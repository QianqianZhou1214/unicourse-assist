from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query: str, context: str) -> str:
    """
    Use OpenAI GPT to generate final answers
    """
    prompt = f"""
    You are an AI assistant. Use the following context to answer the question.

    User Question: {query}
    Context: {context}

    Please provide a detailed and accurate answer.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]