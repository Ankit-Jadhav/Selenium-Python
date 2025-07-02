import requests
import random 
import json
import string

#base url
base_url ="https://gorest.co.in"

#Auth_token
auth_token = "eda34ee9a38af296627feeec00952e5414fe391dc2c5fb0cfb659dabff8c9b38"

#GET_Request
def get_request():
    url = base_url + "/public/v2/users"
    print("get_url:" + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code ==200
    json_data= response.json()
    json_str= json.dumps(json_data, indent= 4)    #beautify json
    print("json response body: ", json_str )

#POST_Request
def post_request():
    url = base_url + "/public/v2/users"
    print("post_url:" + url)
    headers = {"Authorization": auth_token}
    data = {
    "name": "Ankit Test",
    "gender": "male",
    "email": "arjxnkcndadhav3010@gmail.com",
    "status": "active"}
    response = requests.post(url,headers=headers, json = data)
    assert response.status_code ==201
    json_data= response.json()
    json_str= json.dumps(json_data, indent= 4)    #beautify json
    print("json response body: ", json_str )


#PUT_Request

#DELETE_Request



get_request()
post_request()


