import requests
import json
import warnings
warnings.filterwarnings('ignore')
url = "https://172.27.26.163:9999/des"
headers = {'Content-type':'application/json',
             'Orgin': 'https://172.27.26.163:9999',
             'Referer':'https://172.27.26.163:9999/game/caves.swf'}

f = open('input.txt')
data = '{"password":"555acfd4d3c1b7a398d71e4c1538ad4d","teamname":"Amalgam","plaintext":"password"}'
data = json.loads(data);
cipherTexts = []
for line in f.readlines():
    data["plaintext"] = line.split(',')[0]
    r = requests.post(url, json=data, headers=headers, verify=False);
    if(r.status_code == 200):
        response = json.loads(r.text);
        # print(data["plaintext"], response["ciphertext"])
        # cipherPlain = "{0},{1}\n".format(data["plaintext"], response["ciphertext"])
        cipherPlain = "{0}\n".format(response["ciphertext"])
        cipherTexts.append(cipherPlain)
    else:
        print("Failed");
f.close()
f.close()
# print(cipherTexts[0])

r = open('Responsefile.txt','w')
r.writelines(cipherTexts)
r.close()