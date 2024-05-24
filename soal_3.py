from pprint import pp
from read import vertex_source, graphs
# [[6, 4, 1], [6, 5, 2], [6, 1, 3], [1, 5, 2], [1, 2, 6], [1, 3, 7], [4, 5, 4], [5, 3, 5],[2, 3, 5] ]
# [[1, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 2], [2, 6, 6], [6, 8, 7], [4, 7, 4], [7, 9, 5] ]
# [[3, 2, 1], [3, 6, 2], [3, 5, 3], [2, 1, 2], [2, 5, 6], [2, 6, 7], [2, 4, 4], [5, 6, 4], [5, 8, 5],[5, 7, 5], [4, 7,1], [7,8,1] ]
graph = graphs
nodes = set(list(map(lambda x: x[0], graph)) + list(map(lambda x: x[1], graph)))
source = [vertex_source]
table2 = dict(map(lambda x: (x ,{'jarak': 0}), nodes))
tetangga =list(filter(lambda x: x[0]== source[0] or x[1] == source[0], graph))
node_udah = []
while len(source)> 0:
    for i in graph.copy():
        if i [0] == source[0] and i[1] not in node_udah + source:
            table2[i[1]]['jarak'] +=table2[source[0]]['jarak'] +1
            graph.remove(i)
            source.append(i[1])
        if i [1] == source[0] and i[0] not in node_udah + source:
            table2[i[0]]['jarak'] +=table2[source[0]]['jarak'] + 1
            graph.remove(i)
            source.append(i[0])
    node_udah.append(source.pop(0))
    
terpanjang = max(table2, key=lambda x: table2[x]['jarak'])

pp(table2)
print('vertex terpanjang adalah: ', terpanjang)
print('panjangnya adalah: ', table2[terpanjang]['jarak'])
