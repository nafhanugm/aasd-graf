f = open("data.txt", "r")
read = []
for x in f:
  read.append( list(map(int, x.split())))

vertex_source =  read.pop()[0]
graphs = read[1:]
