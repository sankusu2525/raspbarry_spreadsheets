import json
import requests

def postData(data):
    if(data is None):
        print("params is empty")
        return False
    payload ={
        "data":data
    }
    url = "https://script.google.com/macros/s/AKfycby73_PDboxN2OpZZzZZZZzZZZzzzZZZZZZZZZ_XXXxxxxXXXXc/exec"
    header ={'Content-Type':'application/json',}
    response = requests.post(url,data= json.dumps(payload), headers=header)
    if(response.status_code == 200 and response.text =="success"):
        print("post success!")
        return True
    print (response.text)
    return False

if __name__=='__main__':
    postData("Hello yeah!!")
