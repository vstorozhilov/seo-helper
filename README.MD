# Инструмент автоматического определения тематики веб-страниц

Сервис предназначен для подбора наиболее релевантной темы из заданного списка в соответствии с тематикой запрашиваемой веб-страницы

Сервис использует следующие сторонние api:
- Google custom search JSON api (+ Google custom search engine) - для быстрого сбора информации о страницы
- ChadGPT (api для ChatGPT модели версии 3.5) - для подбора наиболее релевантной тематики из списка заданных исходя из собранной информации о странице

Для деплоя необходимо определить значения следующих переменных окружения:

**CUSTOM_SEARCH_API_KEY** - ключ поиска для Google custom search JSON API

**CUSTOM_ENGINE_ID** - id кастомного поискового движка Google

**URL_TO_SEARCH_API** - URL (format-строка с местозаполнителями для последующих подстановок) для Google custom search JSON API

**CHAD_API_KEY** - ключ для api ChadGPT (ChatGPT)

**TOPICS_FILE_PATH** - путь до csv-файла с тематиками (формат: 2 колонки "Категория" и "Тема", первая строка для названия колонок)

**MESSAGE_TO_GPT_PATTERN** - текст запроса к модели ChatGPT (format-строка с местозаполнителями для последующих подстановок)

Деплой осуществляется при помощи инструмента оркестрирования и контейнеризации docker-compose.<br>Значения переменных окружения задаются через скрытый файлик **.env**.

REST API эндпоинты:

POST:
- **/check_url** - получить тематику для запрашиваемого url<br>
  ```
  request_body: application/json = {
    url : string
  }
  response_body: application/json = {
    category: string,
    theme: string
  }
  ```
- **/check_urls** - получить тематики для запрашиваемого списка url-ов<br>
  ```
  request_body: application/json = [string]
  response_body: application/json = [{
    category: string,
    theme: string,
    url : string
  }]
  ```

Документация к API-сервиса так же доступна после деплоя: **/docs**

**Стек проекта**: Python3.11 + FastAPI async

**Ссылки на документацию используемых API:**

- https://developers.google.com/custom-search/v1/overview?hl=en
- https://developers.google.com/custom-search
- https://chadgpt.ru/api-docs

