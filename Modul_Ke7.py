#Nomor 1

import re
f = open('indonesia.txt', 'r', encoding='latin1')
a = []
teks = f.read()
f.close()
p = r'\s([Mm]e\w+)'
cocok = re.findall(p, teks)
a.append(cocok)
print(a)

#Nomor 2

f = open('indonesia.txt', 'r', encoding='latin1')
b = []
teks = f.read()
f.close()
p = r'\s(di\w+)'
cocok = re.findall(p, teks)
b.append(cocok)
print(b)

#Nomor 3

f = open('indonesia.txt', 'r', encoding='latin1')
c = []
teks = f.read()
f.close()
p = r'\s(di\s\w+)'
cocok = re.findall(p, teks)
c.append(cocok)
print(c)

#Nomor 4

f = open('KEI.html', 'r', encoding='latin1')
teks = f.read()
f.close()
i = r'\s<td>[\d\.\w\/]+</td>'
p = r'(\w+)</a></td>' + i + i + i + r'\s<td>([\d\.\w\/]+)</td>'
cocok = re.findall(p, teks)
cocok1 = [(i[0], float(i[1])) for i in cocok]
print(cocok1)
