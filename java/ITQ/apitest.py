import requests
import pprint

response = requests.post('http://localhost:5000/json/answertest', json={"value" : 123, "text" : "test"})

print(response.json())


""">>> import requests
>>> r = requests.post('http://httpbin.org/post', json={"key": "value"})
>>> r.status_code
200
>>> r.json()
{'args': {},
 'data': '{"key": "value"}',
 'files': {},
 'form': {},
 'headers': {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Connection': 'close',
             'Content-Length': '16',
             'Content-Type': 'application/json',
             'Host': 'httpbin.org',
             'User-Agent': 'python-requests/2.4.3 CPython/3.4.0',
             'X-Request-Id': 'xx-xx-xx'},
 'json': {'key': 'value'},
 'origin': 'x.x.x.x',
 'url': 'http://httpbin.org/post'}"""


"""
x = requests.get("http://localhost:5000/greet/user/sascha")
print(x)
pprint.pprint(x.json())
x = requests.get("http://localhost:5000/random/new?range=13")
print(x)
pprint.pprint(x.json())
x = requests.get("http://localhost:5000/uuid/new")
print(x)
pprint.pprint(x.json())
"""