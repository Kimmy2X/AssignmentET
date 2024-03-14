import requests
import json

#Enter Token
access_token = input("Enter Webex Token: ")

#Verify
url = 'https://webexapis.com/v1/people/me'
headers = {
'Authorization': 'Bearer {}'.format(access_token)
}

#dump and load to a dictionary
userInfo = json.loads(json.dumps(requests.get(url, headers=headers).json(), indent=4))

print("WELCOME " + userInfo['nickName'])

#Option 1: Display user information
print("Display Name: " + userInfo['displayName'])
print("First Name: " + userInfo['firstName'])
print("Last Name: " + userInfo['lastName'])
print("Nickname: " + userInfo['nickName'])
print("Email: " + userInfo['userName'])

#Option 2:  List rooms and details
#list rooms
url = 'https://webexapis.com/v1/rooms'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())

#room details
room_id = input('roomID')
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())

#Option 3: Create Room
roomName = input('Enter your room name')
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': roomName}
res = requests.post(url, headers=headers, json=params)
print(res.json())

#Option 4: Send Message to a room
message = input('Enter Message')
roomName = input('Enter room name')
url = 'https://webexapis.com/v1/messages'
headers = {
'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}
params = {'roomName': roomName, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())

