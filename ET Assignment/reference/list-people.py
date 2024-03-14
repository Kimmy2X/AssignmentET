import requests
import json

access_token = 'MmI5ZDlhOTYtNDMwZC00NDVmLWI3YmItYmE2OTI0MWVkNGVjYTJlMGM4YTEtYzgy_P0A1_7e57d048-2511-4d53-8dd4-05fe61659f5d'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'harrazhasmadi@yahoo.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yMGZkMTljMy1hNDE5LTQ3MzUtODhlMi02MzJlY2Y5MWYyOWQ'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
