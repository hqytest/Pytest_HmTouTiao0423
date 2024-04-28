import random
import sys

import requests
import api

url_articles = api.host + "/mp/v1_0/articles?draft=false"
data = {"title": "hantest" + str(random.randint(100, 999)), "content": "<p>1</p>", "imgType": "single",
        "channel_id": 7,
        "cover": {"type": 1, "images": ["http://toutiao-img.itheima.net/FlroLEiqEi1nKPzWennulkyx3-th"]}}

headers = {'Content-Type': 'application/json', 'Authorization': 'Bear eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDU0NzY0NDgsInVzZXJfaWQiOjEsInJlZnJlc2giOmZhbHNlLCJ2ZXJpZmllZCI6dHJ1ZX0.pugR9LLaA9DhpL5vDl8vO7sw7HV3S8rlbKOH5j4Gr8M'}

# 调用登录的post请求并返回响应对象
# 注意：请求数据的接受参数为json，因为headers中的content-type为json
r = requests.post(url=url_articles, headers=api.headers, json=data)
print(r.json())

print(sys.path)