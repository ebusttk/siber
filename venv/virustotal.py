import requests

params = {'apikey': 'e10bee8920b541b59d9ba3b1b89e94c32cd8e3ec488f781caf4bd47442d67fc6','url':'gazi.edu.tr'}
response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
json_response = response.json()
analiz=json_response['permalink']
print requests.get(url=str(analiz)).content
