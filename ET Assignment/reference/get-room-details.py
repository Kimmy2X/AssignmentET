import requests

access_token = 'MmI5ZDlhOTYtNDMwZC00NDVmLWI3YmItYmE2OTI0MWVkNGVjYTJlMGM4YTEtYzgy_P0A1_7e57d048-2511-4d53-8dd4-05fe61659f5d'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzhmNjA3ODAtZDVlOC0xMWVlLTkwYWMtYzdjMzZjNDUyNGIx'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())
