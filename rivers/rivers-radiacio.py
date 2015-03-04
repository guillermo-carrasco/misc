import csv

data = csv.reader(open('spr.csv'), delimiter=',')
rivers = {}

# Guardamos los rios en un hash para acceder mas rapidamente
for d in data:
    rivers[d[0]] = d


def find_rivers_rec(id, river, ends=False, way={}):
    """
    Encuentra recursivamente el curso de un rio
    """
    dest = river[1]
    if dest == id:
        return True, way
    elif dest and dest not in way and dest in rivers:
        way[dest] = river
        return find_rivers_rec(id, rivers[dest], False, way)
    else:
        return False, {}


def find_rivers_wrtfile(f,id):
    """
    Encuentra todos los rios que desembocan directa o indirectamente en el rio id
    """
    if not rivers.has_key(id):
        print "ERROR: Ese rio no existe :-("
    else:
        enders = []
        for k, v in rivers.iteritems():
            if k != id:
                ends, way = find_rivers_rec(id, v, way={})
                if ends:
                    enders.append(k)
        for float_field in [3, 5, 7, 9]:#Son les columnes que es volen calcular
            try:
                float(rivers[id][float_field])
            except ValueError:
                print "Faltan datos para el rio {}".format(str(id))
            else:
                f.write(id)
                f.write(';')
                totalcatchment = float(rivers[id][2]) + sum(float(rivers[k][2]) for k in enders)
                f.write(str(totalcatchment))
                f.write(';')
                dure = float(rivers[id][4])*float(rivers[id][2]) + sum(float(rivers[k][4]) * float(rivers[k][2])for k in enders)
                f.write(str(dure/totalcatchment))
                f.write(';')
                srd = float(rivers[id][5])*float(rivers[id][2]) + sum(float(rivers[k][5]) * float(rivers[k][2])for k in enders)
                f.write(str(srd/totalcatchment))
                f.write(';')
                dird = float(rivers[id][8])*float(rivers[id][2]) + sum(float(rivers[k][8]) * float(rivers[k][2])for k in enders)
                f.write(str(dird/totalcatchment))
                f.write(';')
                difd = float(rivers[id][9])*float(rivers[id][2]) + sum(float(rivers[k][9]) * float(rivers[k][2])for k in enders)
                f.write(str(difd/totalcatchment))
                f.write('\n')

########################### MAIN
            #Escriu els resultats en la taula
f = open('sprt.csv','w')#Crea taula de radiacions totals
f.write('CODI_BASE;tc;srt;dirt;dift;durt\n')#Escriu les columnes
for id in rivers.keys():
    find_rivers_wrtfile(f,id)
f.close()
