import requests
url = "http://172.17.50.43/spicyx"
r = requests.get(url)
print("Status code:")
print("\t *",r.status_code)

h = requests.head(url)
print("Header:\n /headers.php")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("/headers.php")

url2 = "http://httpbin.org/headers"
headers = {
    'User-Agent':'Mobile'
}
r2 = requests.get (url2,headers = headers)
print(r2.text)
