import requests
i=0
url = 'https://stepik.org/media/attachments/course67/3.6.2/267.txt'
r = requests.get(url)
r=r.text
#print(type(r))
#for x in r:
#    i+=1
    #print(x)
#print(r.text)

# Разбиваем строку на список строк
lines = r.splitlines()

# Выводим результат
for line in lines:
    print(line)
    i+=1
print(i)
