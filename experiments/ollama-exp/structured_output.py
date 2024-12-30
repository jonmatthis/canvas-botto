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

if __name__ == "__main__":
    import asyncio
    ollama_client = get_ollama_client()


    async def chat():
        system_msg = {
            'role': 'system', 
            'content': 'Give answers in JSON format in accordance with the provided schema. Do your best to fulfill the requirements of ths schema in the most direct way possible.'
        }
        message = {
            'role': 'user', 
            'content': 'If Im out there pining for the fjords, where might I be from?'
            }
        response = await AsyncClient().chat(
            model=DEFAULT_OLLAMA_MODEL, 
            messages=[message],
            format=Country.model_json_schema(),
            options={"temperature":0.0}
            )
        # print(response.message.content)
        print(Country.model_validate_json(response.message.content))


    asyncio.run(chat())