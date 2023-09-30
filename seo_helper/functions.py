import json
from fastapi import HTTPException
from httpx import AsyncClient
import os
from .topics_loader import topics

CUSTOM_SEARCH_API_KEY = os.getenv('CUSTOM_SEARCH_API_KEY')
CUSTOM_ENGINE_ID = os.getenv('CUSTOM_ENGINE_ID')
URL_TO_SEARCH_API = os.getenv('URL_TO_SEARCH_API')
CHAD_API_KEY = os.getenv('CHAD_API_KEY')
MESSAGE_TO_GPT_PATTERN = os.getenv('MESSAGE_TO_GPT_PATTERN')

STRING_TOPIC_LIST = ', '.join(topics.keys())


async def get_search_results(url):
    print('get search result start')
    async with AsyncClient() as ac:
        response = await ac.get(URL_TO_SEARCH_API.format(CUSTOM_SEARCH_API_KEY, CUSTOM_ENGINE_ID, url))
    print(response.status_code)
    return response.json() if response.status_code == 200 else {}


def compile_chatgpt_query(url, json_response):
    gpt_query_text = "\"" + url + ". "
    if items:=json_response.get('items'):
        item = items[0]
        gpt_query_text += item['title'] + ". "
        gpt_query_text += item['snippet']
    gpt_query_text += "\""

    print(gpt_query_text)

    return gpt_query_text


async def get_chatgpt_answer(gpt_query_text :  str):
    
    message_to_gpt = MESSAGE_TO_GPT_PATTERN.format(gpt_query_text)

    print(STRING_TOPIC_LIST)

    history_context = {
        "role": "assistant",
        "content": STRING_TOPIC_LIST
    }

    # Формируем запрос
    request_json = {
        "message": message_to_gpt,
        "api_key": CHAD_API_KEY,
        "history" : [history_context]
    }

    async with AsyncClient() as ac:
        response = await ac.post(
            url='https://ask.chadgpt.ru/api/public/gpt-3.5',
            json=request_json
        )

    # Проверяем, отправился ли запрос
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Ошибка запроса к ChadGPT")
    else:
        # Получаем текст ответа и преобразовываем в dict
        resp_json = response.json()

        # Если успешен ответ, то выводим
        if resp_json['is_success']:
            resp_msg = resp_json['response']
            return resp_msg
        else:
            error = resp_json['error_message']
            return f"Ошибка ответа ChadGPT: {error}"