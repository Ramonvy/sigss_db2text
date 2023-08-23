import json

db_full = []

def fuse_db():

    f = open('page_1.txt', errors="ignore")
    line = f.readline()

    if line.count(']}]}') > 1:
        line = line[0: line.index(']}]}') + 4]

    if 'RUA \"E\"' in line:
        line = line.replace('RUA \"E\"', 'RUA E')

    if 'D\"A' in line:
        line = line.replace('D\"A', 'DA')

    data = json.loads(line)
    pages = data['total']
    f.close()

    i = 1
    while i <= pages:
        print(str(i))
        f = open('page_' + str(i) + '.txt', errors="ignore")
        line = f.readline()
        data = json.loads(line)
        data = data['rows']

        for j in range(len(data)):
            db_full.append(data[j]['cell'][10] + '\t' + data[j]['cell'][11] + '\t' + data[j]['cell'][12] + '\t' + data[j]['cell'][13] + '\t' + data[j]['cell'][14] + '\t' + data[j]['cell'][15] + '\t' + data[j]['cell'][16] + '\t' + data[j]['cell'][17] + '\t' + data[j]['cell'][18] + '\t' + data[j]['cell'][23] + '\n')

        i = i + 1



fuse_db()

f = open('db_full.txt', 'w')
for i in range(len(db_full)):
    #print(db_full[i])
    f.write(db_full[i])

f.close()
