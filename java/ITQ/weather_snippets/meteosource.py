
import requests
import pprint

parameters = {'key': 'd9jb9j8ftekzsw6k8ffg8mzki1pe47qa9papl517',
              'place_id': 'london'}

url = "https://www.meteosource.com/api/v1/free/point"

data = requests.get(url, parameters).json()
#pprint.pprint(data)
print(data)
#print('Current temperature in London is {} °C.'.format(data['current']['temperature']))  
