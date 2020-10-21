import json
import urllib.request,urllib.parse,urllib.error

s = 0

url = input("Enter url : \n")
data = urllib.request.urlopen(url).read()
try:
    js = json.loads(data)
except:
    js = None
print("RETRIVING DATA FROM URL : ",url)
print("--------------------")
for line in js["comments"]:
    print(line["count"])
    s = s + int(line['count'])
print("--------------------")
print(s)    