from fastapi import APIRouter
from ..functions import *
from ..topics_loader import topics


router = APIRouter(
    responses={404: {"description": "Not found"}}
)


@router.get("/check_url")
async def check_url(url : str):
    print(topics)
    print(url)
    url = url.replace("&", "")
    print('tuta')
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
