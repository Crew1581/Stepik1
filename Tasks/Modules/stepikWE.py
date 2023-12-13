import requests
i=0
url = 'https://stepik.org/media/attachments/course67/3.6.3/699991.txt'
r = requests.get(url)
r=r.text
r1=r
while True:
    url1='https://stepik.org/media/attachments/course67/3.6.3/'+r1
    r1 = requests.get(url1)
    r1 = r1.text
    if r1.startswith('We'):
        break
print(r1)