import requests
access_token = 'MmI5ZDlhOTYtNDMwZC00NDVmLWI3YmItYmE2OTI0MWVkNGVjYTJlMGM4YTEtYzgy_P0A1_7e57d048-2511-4d53-8dd4-05fe61659f5d'
url = 'https://webexapis.com/v1/rooms'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())
