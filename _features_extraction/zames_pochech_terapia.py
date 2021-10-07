r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('заместительная_почечная_терапия.txt', 'w')


doc = 'ПРОТОКОЛ_ОПЕРАЦИИ_ЗАМЕСТИТЕЛЬНОЙ_ПОЧЕЧНОЙ_ТЕРАПИИ'
doc = doc.lower()

for line in r.readlines():
    a = line.split('\t')
    d = a[10].lower()

    res = '0'
    if d.find(doc) != -1:
        res = '1'
    w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()