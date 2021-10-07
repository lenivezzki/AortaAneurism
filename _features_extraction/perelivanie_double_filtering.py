plazma = ['плазма', 'сзп']

trombo = ['тк', 'тромбоцитный концентрат', 'тромбоциты']

eritro = ['эр']

r = open('переливание_фильтр.txt', 'r')
w = open('переливание_значения.txt', 'w')

import re

for line in r.readlines():
    flag=True
    a = line.split('\t')
    text = ' '+a[4][:-1]+' '
    if a[3] == 'ТРЕБОВАНИЕ_на_выдачу_ГТС':
        for p in plazma:
            if text.find(p) != -1:
                res = re.findall(r'кол во доз \d+', text)
                if len(res) > 0:
                    res = re.sub(r'[а-я ]','',res[0])
                    flag = False
                    w.write(a[0] + '\t' + a[1] + '\t'+a[2]+ '\t' + a[3] +'\t'+'плазма_дозы: '+res+'\n')
        for t in trombo:
            if text.find(t) != -1:
                res = re.findall(r'кол во доз \d+', text)
                if len(res) > 0:
                    res = re.sub(r'[а-я ]','',res[0])
                    flag = False
                    w.write(a[0] + '\t' + a[1] + '\t'+a[2]+ '\t' + a[3] +'\t'+'тромбоциты_дозы: '+res+'\n')
        for e in eritro:
            if text.find(e) != -1:
                res = re.findall(r'кол во доз \d+', text)
                if len(res) > 0:
                    res = re.sub(r'[а-я ]','',res[0])
                    flag = False
                    w.write(a[0] + '\t' + a[1] + '\t'+a[2]+ '\t' + a[3] +'\t'+'эритроциты_дозы: '+res+'\n')

    if a[3] == 'ПРОТОКОЛ_ПЕРЕЛИВАНИЯ_КРОВИ_И_КОМПОНЕНТОВ_КРОВИ':
        for p in plazma:
            if text.find(p) != -1:
                res = re.findall(r' л \d+\.\d+', text)
                if len(res) > 0:
                    res = re.sub(r'[а-я ]','',res[0])
                    flag = False
                    w.write(a[0] + '\t' + a[1] + '\t'+a[2]+ '\t' + a[3] +'\t'+'плазма_объем: '+res+'\n')
        for t in trombo:
            if text.find(t) != -1:
                res = re.findall(r' л \d+\.\d+', text)
                if len(res) > 0:
                    res = re.sub(r'[а-я ]','',res[0])
                    flag = False
                    w.write(a[0] + '\t' + a[1] + '\t'+a[2]+ '\t' + a[3] +'\t'+'тромбоциты_объем: '+res+'\n')
        for e in eritro:
            if text.find(e) != -1:
                res = re.findall(r' л \d+\.\d+', text)
                if len(res) > 0:
                    res = re.sub(r'[а-я ]','',res[0])
                    flag = False
                    w.write(a[0] + '\t' + a[1] + '\t'+a[2]+ '\t' + a[3] +'\t'+'эритроциты_объем: '+res+'\n')
        if text.find('количество перелитой среды') != -1:
            res_vol = re.findall(r'\d+\.\d+ л', text)
            res_doz = re.findall(r'\d+ доз', text)
            if (len(res_vol) == 0):
                vol = '-1'
            else:
                vol = re.sub(r'[а-я ]', '', res_vol [0])
            if (len(res_doz) == 0):
                doz = '-1'
            else:
                doz = re.sub(r'[а-я ]', '', res_doz[0])
            flag = False
            w.write(a[0] + '\t' + a[1] + '\t'+a[2]+ '\t' + a[3] + '\t' + 'всего_объем: ' + vol + '; всего_доз: ' + doz + '\n')
    if flag:
        print()
r.close()
w.close()