import requests

access_token = 'MmI5ZDlhOTYtNDMwZC00NDVmLWI3YmItYmE2OTI0MWVkNGVjYTJlMGM4YTEtYzgy_P0A1_7e57d048-2511-4d53-8dd4-05fe61659f5d'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzhmNjA3ODAtZDVlOC0xMWVlLTkwYWMtYzdjMzZjNDUyNGIx'
person_email = 'harrazhasmadi@yahoo.com'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())
