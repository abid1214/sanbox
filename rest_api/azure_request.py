import requests
import json

tenantId = "44467e6f-462c-4ea2-823f-7800de5434e3"
clientId = "c6f7c55e-fb93-4a6d-b778-0e2b41f8d76f"
clientSecret = "27f79d0f-696c-4b0c-84d3-23911edc6933"
subscriptionId = "f9a125bf-3cf4-40aa-9fb5-e21041159d9d"
resourceGroupName = "Testing"


resource = "https://management.azure.com/"
url = "https://login.microsoftonline.com/"+tenantId+"/oauth2/token"
payload = "grant_type=client_credentials&client_id="+clientId+"&client_secret="+clientSecret+ \
        "&resource=https%3A%2F%2Fmanagement.azure.com%2F&undefined="
headers = {'Content-Type': "application/x-www-form-urlencoded"}
response = requests.request("POST", url, data=payload, headers=headers)

data = json.loads(response.text)
token_type = data["token_type"]
access_token = data["access_token"]

url = "https://management.azure.com/subscriptions/" + subscriptionId + "/resourcegroups/"+\
        resourceGroupName + "/exportTemplate"
querystring = {"api-version":"2019-05-10"}
payload = "{\n  \"resources\": [\n    \"*\"\n  ]\n}"
headers = {'Content-Type': "application/json", 'Authorization': token_type + " " + access_token}
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

data = json.loads(response.text)['template']
resourceGroups = json.dumps(data, indent=2, default=str)
with open("resources.json", 'w') as fp:
    fp.write(resourceGroups)
