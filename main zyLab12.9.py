# Luis Arroyo
# PSID: 2037081
# CIS 2348

#empty list
list=[]

#getting input, break
while (True):
    entry = input()
    name=entry.split(' ')[0]
    if entry == '-1':
        break
    try:
        age=int(entry.split(' ')[1])
    except:
        age=0
    list.append([name,age])
#output name then added age.
for f in list:
    if f[1] != 0:
        print(f'{f[0]} {(f[1] + 1)}')
    else:
        print(f'{f[0]} {f[1]}')
        # raise ValueError
