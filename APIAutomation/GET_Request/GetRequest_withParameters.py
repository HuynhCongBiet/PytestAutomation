import requests
param = {'name':'Biet Huynh', 'email':'biethuynh@gmail.com', 'sdt':'0987219023', 'address': 'TP.HCM'}
response = requests.get("https://httpbin.org/get", params=param)
print(response.text)