#!/usr/local/bin/python3
import requests, json, urllib.request

apiUrl = "https://api.generated.photos/api/v1/faces"
authKey = "-zVkVl7metLq9EJrF55oYw"  # 발급받은키

headers = {
    'Authorization': 'API-Key ' + authKey
}

data = {
    'gender': 'female',
    'ethnicity': 'asian',
    'age': 'young-adult',
}

# urllib가 아닌 requests 라이브러리 별도로 설치해서 통신하고 있을 때
response = requests.get(apiUrl, headers=headers, data=data)
resultJson = json.loads(response.text)

for face in resultJson["faces"]:
    id = face["id"]
    imageUrl = face["urls"][4]["512"]
    #filePath = "./result/" + id + ".jpg"
    filePath = "/Users/user/Desktop/test/" + id + ".jpg"
    urllib.request.urlretrieve(imageUrl, filePath)
    print(filePath)

