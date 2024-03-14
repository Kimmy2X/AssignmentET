import requests
import json

access_token = 'MDM3MmEwY2MtZjA1YS00MzgwLTk1NzgtNDM2MjZmZDFlYzEwOTgwOWM2ODMtMDFh_P0A1_7e57d048-2511-4d53-8dd4-05fe61659f5d'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
