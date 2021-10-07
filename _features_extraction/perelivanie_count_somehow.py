r = open('переливание_значения oper_period no_povtor.txt', 'r')

dozi_trebovanie = {}

dozi_perelivanie = {}

def find_max(p, t, e):
    p_max = -1.0
    t_max = -1.0
    e_max = -1.0
    if len(p) > 0:
        for i in range(len(p)):
            p[i] = re.sub(r'[а-я _:]+','',p[i])
        p_max = float(max(p))
    if len(t) > 0:
        for i in range(len(t)):
            t[i] = re.sub(r'[а-я _:]+','',t[i])
        t_max = float(max(t))
    if len(e) > 0:
        for i in range(len(e)):
            e[i] = re.sub(r'[а-я _:]+','',e[i])
        e_max = float(max(e))
    if (p_max > t_max) & (p_max > e_max):
        return 'плазма'
    if (t_max > p_max) & (t_max > e_max):
        return 'тромбоциты'
    if (e_max > p_max) & (e_max > t_max):
        return 'эритроциты'


#def def_plazma(mas):
#    if len(mas) > 0:

prev_doc = 'ПРОТОКОЛ_ПЕРЕЛИВАНИЯ_КРОВИ_И_КОМПОНЕНТОВ_КРОВИ'
prev_id = ''
trebovanie = [0,0,0]

import re

for line in r.readlines():
    line = line[:-1]
    a = line.split('\t')
    if a[0] not in dozi_perelivanie:
        dozi_perelivanie[a[0]] = {'plazma':[],
                                  'trombo':[],
                                  'eritro':[]}
    text = a[5]
    if a[4] == 'ТРЕБОВАНИЕ_на_выдачу_ГТС':
        p = re.findall(r'плазма_дозы: \d+', text)
        t = re.findall(r'тромбоциты_дозы: \d+', text)
        e = re.findall(r'эритроциты_дозы: \d+', text)
        if len(p) > 0:
            p = re.sub(r'[а-я _:]+','',p[0])
        else:
            p = '0'
        if len(t) > 0:
            t = re.sub(r'[а-я _:]+', '', t[0])
        else:
            t = '0'
        if len(e) > 0:
            e = re.sub(r'[а-я _:]+', '', e[0])
        else:
            e = '0'
        if prev_doc == 'ТРЕБОВАНИЕ_на_выдачу_ГТС':
            trebovanie[0] += int(p)
            trebovanie[1] += int(t)
            trebovanie[2] += int(e)
        else:
            trebovanie = [int(p), int(t), int(e)]


    if prev_id != a[0]:
        if prev_doc != 'ПРОТОКОЛ_ПЕРЕЛИВАНИЯ_КРОВИ_И_КОМПОНЕНТОВ_КРОВИ':
            prev_id = a[0]
    prev_doc = a [4]

    if a[4] == 'ПРОТОКОЛ_ПЕРЕЛИВАНИЯ_КРОВИ_И_КОМПОНЕНТОВ_КРОВИ':
        p = re.findall(r'плазма_объем: \d\.\d+', text)
        t = re.findall(r'тромбоциты_объем: \d\.\d+', text)
        e = re.findall(r'эритроциты_объем: \d\.\d+', text)
        d = re.findall(r'всего_доз: -?\d', text)
        if len(d) > 0:
            d = re.sub(r'[а-я _:]+', '', d[0])
        else:
            d = '2'


        sum_len = len(p) + len(t) + len(e)
        num_d = int(d)

        #отслеживание потенциальных ошибок
#        if (num_d > sum(trebovanie)+2) & (prev_id == a[0]):
#            print() #присвоить дозу как в требованиях? или если в требованиях 1 а на переливании 5 if 1 in trebovania and d = 5

        #если кол-во компонент совпадает с кол-вом доз
        if sum_len == num_d:
            dozi_perelivanie[a[0]]['plazma'].append(len(p))
            dozi_perelivanie[a[0]]['trombo'].append(len(t))
            dozi_perelivanie[a[0]]['eritro'].append(len(e))
            trebovanie[0] -= len(p)
            trebovanie[1] -= len(t)
            trebovanie[2] -= len(e)
            continue

        #если кол-во компонент на 1 меньше кол-ва доз
        if (sum_len+1) == num_d:
            dozi_perelivanie[a[0]]['plazma'].append(len(p))
            dozi_perelivanie[a[0]]['trombo'].append(len(t))
            dozi_perelivanie[a[0]]['eritro'].append(len(e))
            trebovanie[0] -= len(p)
            trebovanie[1] -= len(t)
            trebovanie[2] -= len(e)
            who_max = find_max(p,t,e)
            if who_max == 'плазма':
                dozi_perelivanie[a[0]]['plazma'].append(1)
                trebovanie[0] -= 1
            if who_max == 'тромбоциты':
                dozi_perelivanie[a[0]]['trombo'].append(1)
                trebovanie[1] -= 1
            if who_max == 'эритроциты':
                dozi_perelivanie[a[0]]['eritro'].append(1)
                trebovanie[2] -= 1
            continue

        #если доз 0, а компоненты есть (ошибка) PS обычно это значит что объем маленький ~170
        if (num_d == 0) & (sum_len != 0):

            dozi_perelivanie[a[0]]['plazma'].append(len(p))#добавляем хотя бы те, что перечислены, без учета объема
            dozi_perelivanie[a[0]]['trombo'].append(len(t))
            dozi_perelivanie[a[0]]['eritro'].append(len(e))
            trebovanie [0] -= len(p)
            trebovanie [1] -= len(t)
            trebovanie [2] -= len(e)
            continue

        #если доз меньше числа компонент (ошибка?)
        if (num_d < sum_len):
            dozi_perelivanie[a[0]]['plazma'].append(len(p))#добавляем те, что перечислены, без учета объема
            dozi_perelivanie[a[0]]['trombo'].append(len(t))
            dozi_perelivanie[a[0]]['eritro'].append(len(e))
            trebovanie[0] -= len(p)
            trebovanie[1] -= len(t)
            trebovanie[2] -= len(e)
            continue

        if sum_len > num_d:
            print()

r.close()

w = open('переливание_крови_дозы.txt', 'w')

for k in dozi_perelivanie.keys():
    p = sum(dozi_perelivanie[k]['plazma'])
    t = sum(dozi_perelivanie[k]['trombo'])
    e = sum(dozi_perelivanie[k]['eritro'])
    #w.write(k + '\t' + 'плазма_дозы: '+str(p)+'\t'+'тромбоциты_дозы: '+str(t)+'\t'+'эритроциты_дозы: '+str(e)+'\n')
    w.write(k + '\t' + str(p) + '\t'+ str(t) + '\t' + str(e) + '\n')
w.close()



