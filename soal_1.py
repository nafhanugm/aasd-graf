from pprint import pp
from read import vertex_source, graphs
# [[6, 4, 1], [6, 5, 2], [6, 1, 3], [1, 5, 2], [1, 2, 6], [1, 3, 7], [4, 5, 4], [5, 3, 5],[2, 3, 5] ]
graph = graphs
nodes = set(list(map(lambda x: x[0], graph)) + list(map(lambda x: x[1], graph)))
source = vertex_source
table2 = dict(map(lambda x: (x ,{'bobot': 1000000 if x != source else 0, 'parent': None, 'dicoret': False}), nodes))

def belom_dicoret(table_input):
    belom_dicoret = {}
    for k, v in table_input.items():
        if v['dicoret'] == False:
            belom_dicoret[k] = v
    return belom_dicoret

while(list(filter(lambda x: table2[x]['dicoret'] == False, table2)) != []):
    tabel_not_dicoret = belom_dicoret(table2)
    source = min(tabel_not_dicoret,  key=lambda x: tabel_not_dicoret[x]['bobot'])
    tetangga =list(filter(lambda x: x[0]== source or x[1] == source, graph))
    for i in tetangga:
        if i[2] + table2[i[0]]['bobot'] < table2[i[1]]['bobot'] and i[0] == source:
            table2[i[1]]['bobot'] = i[2] + table2[i[0]]['bobot']
            table2[i[1]]['parent'] = i[0]
            

        if i[2] + table2[i[1]]['bobot'] < table2[i[0]]['bobot'] and i[1] == source:
            table2[i[0]]['bobot'] = i[2] + table2[i[1]]['bobot']
            table2[i[0]]['parent'] = i[1]
           
    table2[source]['dicoret']= True

def jarak_terdekat(tabel_final):
    terdekat = max(tabel_final, key=lambda x : tabel_final[x]['bobot'])
    return {
        'vertex terdekat tertinggi': terdekat,
        'jaraknya': table2[terdekat]['bobot']
    }
pp(table2)
pp(jarak_terdekat(table2))
