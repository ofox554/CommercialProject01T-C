import requests
import json
url = "https://api.sandbox.breathehr.info:443/v1/employees?page=1"
accessKey = "sandbox-wZrvSFSWWI9X_0d4oCwmIuWEXI8p-Y9fhM0vFRSOHbo"
headers = {
    'Accepts': 'application/json',
    'X-API-KEY': accessKey,
}
response_API = requests.get(url, headers=headers)
print(response_API.status_code)
print(response_API.json())


json_object = json.dumps(response_API, indent=4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)



