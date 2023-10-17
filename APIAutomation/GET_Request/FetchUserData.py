import requests
import json
import jsonpath
# API URL
url = "https://reqres.in/api/users?page=2"

# Send GET Request
response = requests.get(url)
# print(response)

# Display response content
# print(response.content)
# print(response.status_code)

# Parse response to Json format
json_response = json.loads(response.text)
# print(json_response)

# Fetch value using Json Path basic
# pages = jsonpath.jsonpath(json_response,'pages')
# print(pages[0])
# assert pages[0] == 2

# Fetch value using Json Path advanced
for i in range(0,6):
    first_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(first_name[0])

# Validate the status code
assert response.status_code == 200

# Fetch Response Specific Header
# print(response.headers)
# print(response.headers.get("Date"))
# print(response.headers.get("Server"))

# Fetch Cookies
# print(response.cookies)

# Fetch Encoding
# print(response.encoding)

# Fetch Elapsed Time
# print(response.elapsed)

#