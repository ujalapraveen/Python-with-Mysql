import requests
import json
jira_url= "https://ujalaparveen.atlassian.net/rest/api/2/search#"

headers={
    "Accept":"application/json",
    "Content-Type":"application/json"
}

response_jira=requests.get(jira_url,headers=headers,auth=("ujalaparveen20@navgurukul.org","1YGAgWQh45TaEmarMUJjC51D"))
# print(response_jira)

Data=response_jira.json()
issues=Data["issues"]
# print(issues)
for a in issues:
    b=a["fields"]
    # print(b)
    for x in b["status"]:
        pass
    name=(b["status"]["name"])
    # print(b)
    id=(b["status"]["id"])
    # print(id)
    for y in b["reporter"]:
        pass
    print(b["reporter"]["displayName"]) 
    print(b["reporter"]["emailAddress"]) 
    print(b["description"])
    print(b["updated"])
