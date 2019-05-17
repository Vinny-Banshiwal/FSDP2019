import requests
url1="http://free.currencyconverterapi.com/api/v5/convert"
url2="?q=USD_INR&compact=y"
url3=" &apiKey=fd99ceabc75b8029926b"
url=url1+url2+url3
response=requests.get(url)
response.content

data=response.json()


value=data['results']['USD_INR']['val']
user_input=int(input("enter value"))
INR=user_input*value
print(INR)