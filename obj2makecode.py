from itertools import combinations
# read the file monkey.obj to lines

with open('monkey.obj', 'r') as f:
    lines = f.readlines()

verts = "cv = ["
vertex_list = []
for line in lines:
    line = line.strip()
    if line.startswith('v '):
        x = line.split(' ')[1]
        y = line.split(' ')[2]
        z = line.split(' ')[3]
        vertex_list.append((float(x), float(y), float(z)))
        verts += "  ({}*size, {}*size, {}*size),\n".format(x, y, z)

verts += "]"

edges = ""

for line in lines:
    line = line.strip()
    if line.startswith('f '):

        # line format: draw_line(cv[0][0], cv[0][1], cv[0][2], cv[1][0], cv[1][1], cv[1][2])
        
        v1 = line.split(' ')[1]
        v2 = line.split(' ')[2]
        v3 = line.split(' ')[3]

        v1 = int(v1.split('/')[0]) - 1
        v2 = int(v2.split('/')[0]) - 1
        v3 = int(v3.split('/')[0]) - 1

        vert_list = [v1, v2, v3]

        for edge in combinations(vert_list, 2):
            edges += "draw_line(cv[{}][0], cv[{}][1], cv[{}][2], cv[{}][0], cv[{}][1], cv[{}][2]);\n".format(edge[0], edge[0], edge[0], edge[1], edge[1], edge[1])
            
        


mat = ""



tri_list = []
for line in lines:
    if line.startswith('usemtl '):
        mat = line.split(' ')[1].strip()

    if line.startswith('f '):
        # format is: fill_tri(x1, y1, z1, x2, y2, z1, x3, y3, z3)

        v1 = line.split(' ')[1]
        v2 = line.split(' ')[2]
        v3 = line.split(' ')[3]

        v1 = int(v1.split('/')[0]) - 1
        v2 = int(v2.split('/')[0]) - 1
        v3 = int(v3.split('/')[0]) - 1

        tri_list.append((v1, v2, v3, mat))

# sort the tris to make the ones with a lower z value appear first
tri_list.sort(key=lambda x: (vertex_list[x[0]][2] + vertex_list[x[1]][2] + vertex_list[x[2]][2])/3)


tris = "tris = ["
for tri in tri_list:
    print(tri)

        # tris += "  (cv[{}][0], cv[{}][1], cv[{}][2], cv[{}][0], cv[{}][1], cv[{}][2], cv[{}][0], cv[{}][1], cv[{}][2], {}),\n".format(v1, v1, v1, v2, v2, v2, v3, v3, v3, mat)
    tris = tris + "  (cv[{}][0], cv[{}][1], cv[{}][2], cv[{}][0], cv[{}][1], cv[{}][2], cv[{}][0], cv[{}][1], cv[{}][2], {}),\n".format(tri[0], tri[0], tri[0], tri[1], tri[1], tri[1], tri[2], tri[2], tri[2], tri[3])

tris += "]"





with open('edges.txt' , 'w') as f:
    f.write(edges)

with open('verts.txt' , 'w') as f:
    f.write(verts)


with open('tris.txt' , 'w') as f:
    f.write(tris)