import sys
import csv
import scipy.io.wavfile as sc
import numpy as np
import base64
import wave

maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

# writing wav
        
with open("data/KSU_MobileCreativeSB.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        # print(row[5])
        
        s = base64.b64decode(row[5])
        print(s)
        # writing transcripts :
        
        # out_file_name = 'data/gale/' + row[0] + '.wav'
        # output = wave.open(out_file_name, 'wb')
        # output.setparams((1,1 , 16000, 0, 'NONE', 'not compressed'))
        # output.writeframes(s)


# getting phones

# phones = set()

# with open("data/GALE3_lev.dict") as file_in:
#     for line in file_in:
#         line = line.strip()
#         line = line.split()
#         line = line[1:]
#         for word in line:
#             phones.add(word)

# out = ""
# for phn in phones:
#     out += phn + '\n'

# file_out = open("data/phones_lev.txt", 'w')
# file_out.write(out)

# phns = ['c', 'j', 'w', 'm', 'hm', 'r', 'k', 'f' 'zh', 'hmi', 'v', 'd', 'g', 'e', 't',
#         's', 'q', 'sd', 'u', 'tt', 'h', 'i', 'hma', 'hh', 'th', 'aa', 'b', 'l',
#         'n', 'hmw', 'dd', 'gn', 'x', 'z', 'y']

