r = open('операции нисходящий_отдел_и_выше.txt', 'r')

list_oper = []
for line in r.readlines():
    list_oper.append(line[:-1])
r.close()

r = open('переливание_значения.txt', 'r')
list_write = []
list_num=[]
for line in r.readlines():
    a = line.split('\t')
    list_write.append(a[0]+'\t'+a[1])
    list_num.append('\t'.join(a[2:]))
r.close()

w = open('переливание_значения oper_period.txt', 'w')
for i in range(len(list_write)):
    iddate = list_write[i].split('\t')
    for j in range(len(list_oper)):
        oper = list_oper[j].split('\t')
        if oper[0]==iddate[0]:
            start = int(oper[1])
            end = int(oper[2])
            if (int(iddate[1]) >= start) & (int(iddate[1]) <= end):
                w.write(iddate[0]+'|'+oper[1]+oper[2]+'\t'+list_write[i]+'\t'+list_num[i])
w.close()