import logging
from ollama import AsyncClient
from pydantic import BaseModel

OLLAMA_ASYNC_CLIENT = None

DEFAULT_OLLAMA_MODEL = 'llama3.2'
def get_ollama_client () -> AsyncClient:
    global OLLAMA_ASYNC_CLIENT
    if OLLAMA_ASYNC_CLIENT is None:
        OLLAMA_ASYNC_CLIENT = AsyncClient()
    return OLLAMA_ASYNC_CLIENT


# if using the openai sdk
# client = OpenAI(base_url:"http://localhost:11434/v1", api_key="ollama")

class Country(BaseModel):
    name: str
    capital: str
    languages: list[str]

class TechnicalQuestion(BaseModel):
    question: str
    answer: str

class CheckResult(BaseModel):
    question: str
    result: bool

logging.basicConfig(level=logging.INFO)

async def get_answers(questions: list[str]) -> list[TechnicalQuestion]:
    client = get_ollama_client()
    answers = []
    for question in questions:
        message = {'role': 'user', 'content': question}
        response = await client.chat(
            model=DEFAULT_OLLAMA_MODEL,
            messages=[message],
            format=TechnicalQuestion.model_json_schema(),
            options={"temperature": 0.0}
        )
        answer = TechnicalQuestion.model_validate_json(response.message.content)
        answers.append(answer)
        logging.info(f"Question: {question}, Answer: {answer.answer}")
    return answers

async def check_answers(answers: list[TechnicalQuestion]) -> list[CheckResult]:
    client = get_ollama_client()
    results = []
    for answer in answers:
        message = {'role': 'user', 'content': answer.answer}
        response = await client.chat(
            model=DEFAULT_OLLAMA_MODEL,
            messages=[message],
            format=CheckResult.model_json_schema(),
            options={"temperature": 0.0}
        )
        result = CheckResult.model_validate_json(response.message.content)
        results.append(result)
        logging.info(f"Answer: {answer.answer}, Check Result: {result.result}")
    return results

async def process_questions(questions: list[str], max_retries: int = 5):
    retries = 0
    while retries < max_retries:
        answers = await get_answers(questions)
        check_results = await check_answers(answers)
        questions = [result.question for result in check_results if not result.result]
        if not questions:
            break
        retries += 1
        logging.info(f"Retrying {len(questions)} questions, Attempt {retries}")

if __name__ == "__main__":
    import asyncio
    questions = [
        "What is the capital of France?",
        "What is the largest planet in our solar system?",
        # Add more questions as needed
    ]
    asyncio.run(process_questions(questions))