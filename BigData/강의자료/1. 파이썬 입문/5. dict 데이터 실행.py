a = {'name' : '일선', '수학': 80, '과학':90}

print(a)
print(a['name'])
print(a['수학'])

print(a.keys()) # 딕셔너리의 키 불러오기 
print(a.values()) # 딕셔너리의 값 불러오기 

import requests

url = "http://ip-api.com/json/naver.com"
data = requests.get(url)
data = data.json()
print(data['lat'],data['lon'])
