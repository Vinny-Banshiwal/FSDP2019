import json
import requests

Host = "http://httpbin.org/post"
data={ "Name": 
    "Currency Converter Convert  from USD to INR",
  "Filename": 
    "currecncyconv.py",
  "Problem Statement":
    "You need to fetch the current conversion prices from the JSON  using REST API",
  }
    
response=requests.post(Host,data)
response.text
print(response.text)    
#headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}
#
#def post_method():
#    response = requests.post(Host,data,headers)
#    return response

#print ( post_method().text )


]def get_method():
    response = requests.get("http://httpbin.org/get?firstname=Dev&language=English")
    return response

print (get_method().text)

