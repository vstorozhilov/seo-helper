from fastapi import APIRouter
from ..functions import *
from ..topics_loader import topics
from pydantic import BaseModel

class Url(BaseModel):
    url: str


router = APIRouter(
    responses={404: {"description": "Not found"}}
)


@router.post("/check_url")
async def check_url(url : Url):
    url = url.model_dump()['url']
    url = url.replace("&", "")
    json_response = await get_search_results(url)
    gpt_query_text = compile_chatgpt_query(url, json_response)
    topic = await get_chatgpt_answer(gpt_query_text)
    if topic.startswith("Ошибка ответа ChadGPT:"):
        return topic
    else:
        return {
            "category" : topics[topic] if topic in topics else 'unknown',
            "theme" : topic
        }
