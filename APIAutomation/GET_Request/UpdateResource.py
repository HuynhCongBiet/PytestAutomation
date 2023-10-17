import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"

# Read input from Json file
file = open('C:\\Users\\bhuynh\\Desktop\\CreateUser.json', 'r')
json_input = file.read()
json_request = json.loads(json_input)
# print(request_json)

# Make PUT request with Json input body
response = requests.put(url, json_request)

# Validating the code response
assert response.status_code == 200

# Parse response Content
json_response = json.loads(response.text)
update_li = jsonpath.jsonpath(json_response,'updatedAt')
print(update_li[0])
