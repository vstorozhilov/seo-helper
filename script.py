# import asyncio, requests_async
# from datetime import datetime
# from pprint import pprint

# with open('test_urls.txt', 'r', encoding='utf-8') as f:
#     urls = [x.strip('\n') for x in f.readlines()]

# async def mmain(urls):
#     tasks = [
#         requests_async.post(
#             url='http://127.0.0.1:5000/check_url',
#             json={ 'url' : x }
#         )
#         for x in urls
#     ]
#     return await asyncio.gather(*tasks)

# start = datetime.now()
# results = [x.json() if x.status_code == 200 else
#            'status code: {}'.format(x.status_code)
#            for x in asyncio.run(mmain(urls[80:90]))]
# end = datetime.now()
# print(end - start)
# pprint(results, compact=True, depth=3)

a = {1 : 2, 3 : 4}

for key, val in zip(a, range(2)):
    print(key, val)