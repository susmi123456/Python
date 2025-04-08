import requests

resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
users=resp_data.json()
print(type(users))