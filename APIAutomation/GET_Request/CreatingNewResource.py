import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read input from Json file
file = open('C:\\Users\\bhuynh\\Desktop\\CreateUser.json', 'r')
json_input = file.read()
json_request = json.loads(json_input)
# print(request_json)

# Make Post request with Json input body
response = requests.post(url, json_request)

# Validating the code response
assert response.status_code == 201

# Fetch header from Response
# print(response.headers)
# print(response.headers.get('Content-Length'))

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)

# Pick ID using Json Path
id = jsonpath.jsonpath(json_response,'id')
print(id[0])