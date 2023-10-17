import requests

# API URL
url = "https://reqres.in/api/users/"

response = requests.delete(url)
print(response.status_code)

# Fetch response code
status_code = response.status_code
assert status_code == 204