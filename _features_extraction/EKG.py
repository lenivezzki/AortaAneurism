r = open('data.txt', 'r')
w = open('ЭКГ_beta.txt', 'w')

dict = {}

import re

header = 'RR\tP\tPQ\tQRS\tQT\tL\tRS\tЧСС'

for line in r.readlines():
    res = []

    if line.find('ЭКГ_РЕЗУЛЬТАТ') != -1:
        line = line.lower()
        if line.find('rr') != -1:
            i = re.findall('rr\s?\d+', line)
            if len(i) >= 1:
                res.append(i[0])


    if line.find('ЭКГ_РЕЗУЛЬТАТ') != -1:
        line = line.lower()
        if line.find('p') != -1:
            i = re.findall('p\s?\d+', line)
            if len(i) >= 1:
                res.append(i[0])


    if line.find('ЭКГ_РЕЗУЛЬТАТ') != -1:
        line = line.lower()
        if line.find('pq') != -1:
            i = re.findall('pq\s?\d+', line)
            if len(i) >= 1:
                res.append(i[0])


    if line.find('ЭКГ_РЕЗУЛЬТАТ') != -1:
        line = line.lower()
        if line.find('qrs') != -1:
            i = re.findall('qrs\s?\d+', line)
            if len(i) >= 1:
                res.append(i[0])

    if line.find('ЭКГ_РЕЗУЛЬТАТ') != -1:
        line = line.lower()
        if line.find('qt') != -1:
            i = re.findall('qt\s?\d+', line)
            if len(i) >= 1:
                res.append(i[0])

    if line.find('ЭКГ_РЕЗУЛЬТАТ') != -1:
        line = line.lower()
        if line.find('l') != -1:
            i = re.findall('l\s?\d+', line)
            if len(i) >= 1:
                res.append(i[0])


    if line.find('ЭКГ_РЕЗУЛЬТАТ') != -1:
        line = line.lower()
        if line.find('rs') != -1:
            i = re.findall('rs\s?\d+', line)
            if len(i) >= 1:
                res.append(i[0])


    if line.find('ЭКГ_РЕЗУЛЬТАТ') != -1:
        line = line.lower()
        if line.find('чсс') != -1:
            i = re.findall('чсс\s?\d+', line)
            if len(i) >= 1:
                res.append(i[0])


    if len(res)>=1:
        a = line.split('\t')
        if a[1] in dict:
            dict[a[1]] = dict[a[1]] + '\t' + '\t'.join(res)
        else:
            dict[a[1]] = a[1] + '\t' + '\t'.join(res)

for d in dict:
    w.write(d + '\n')

