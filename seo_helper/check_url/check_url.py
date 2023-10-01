from fastapi import APIRouter
from ..functions import *
from ..topics_loader import topics
from pydantic import BaseModel

class Url(BaseModel):
    url: str

class Urls(BaseModel):
    urls: list[str]

class Topic(BaseModel):
    category: str
    theme: str

class TopicWithURL(BaseModel):
    url : str
    category: str
    theme: str

router = APIRouter(
    responses={404: {"description": "Not found"}}
)


@router.post("/check_url")
async def check_url(url : Url) -> Topic:
    url = url.model_dump()['url']
    json_response = await get_search_results(url)
    gpt_query_text = compile_chatgpt_query(url, json_response)
    topic = await get_chatgpt_answer(gpt_query_text)
    return Topic(
        category=topics[topic] if topic in topics else 'unknown',
        theme=topic
    )

@router.post("/check_urls")
async def check_urls(urls : Urls) -> list[TopicWithURL]:
    urls = urls.model_dump()['urls']
    json_responses = await get_search_results_batch(urls)
    gpt_query_texts = [compile_chatgpt_query(url, json_response) for
                       url, json_response in zip(urls, json_responses)]
    topics_fetched = await get_chatgpt_answers_batch(gpt_query_texts)
    response_json = []
    for topic, url in zip(topics_fetched, urls):
         response_json.append(TopicWithURL(
            url=url,
            category=topics[topic] if topic in topics else 'unknown',
            theme=topic
        ))
    return response_json
