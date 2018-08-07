file_in = './data/GALE3.hyp'

line = open(file_in, 'r').read().splitlines()
for l in line:
    end = l.split()
    print( end)