import requests
access_token = 'NTY1YTUyYjMtM2NiYi00YmE0LWJiMzAtMWZlZmYwM2M1M2Q0OWEzNTA2NWItYjcw_P0A1_7e57d048-2511-4d53-8dd4-05fe61659f5d'
room_id = 'your_room_id'
url = 'https://webexapis.com/v1/memberships'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())
