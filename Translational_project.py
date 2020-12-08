import pandas as pd

import os

from pandas import DataFrame

import os

os.chdir('./')

SpikeMut = pd.read_csv('./Spike Mutation G.fasta', sep='\t')

SpikeMut_location = SpikeMut.iloc[:,0]

Sstring = " "

count = 0 
for row in SpikeMut_location:
    for value in row:
        count += 1
        if 21563 <= count >= 25384:
            Sstring = Sstring + value + " "

def remove(string): 
    return string.replace(" ", "")
            
            
Sstring = remove(Sstring)

count = 0
for i in Sstring:
    count += 1

text_file = open("spike_M_from_python.txt", "w")
n = text_file.write(Sstring)
text_file.close()



################
#Nucleo


NucleoMut = pd.read_csv('./Nucleocapsid Mutation M.fasta', sep='\t')

Nucleostring = " "


NucleoMut_location = NucleoMut.iloc[:,0]

count = 0 
for row in NucleoMut_location:
    for value in row:
        count += 1
        if 28274 <= count >= 29533:
            Nucleostring = Nucleostring + value + " "

#reference
#https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
def remove(string): 
    return string.replace(" ", "")
            
            
            

Nucleostring = remove(Nucleostring)

count = 0
for i in Nucleostring:
    count += 1

#print(count)

text_file = open("Nucleo_M_from_python.txt", "w")
n = text_file.write(Nucleostring)
text_file.close()


#################

#Envelope


EnvMut = pd.read_csv('./Envelope Mutation F.fasta', sep='\t')

Envstring = " "


EnvMut_location = EnvMut.iloc[:,0]

count = 0 
for row in EnvMut_location:
    for value in row:
        count += 1
        if 26245 <= count >= 26472:
            Envstring = Envstring + value + " "

#reference
#https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
def remove(string): 
    return string.replace(" ", "")
                      

Envstring = remove(Envstring)

count = 0
for i in Envstring:
    count += 1

#print(count)

text_file = open("Env_M_from_python.txt", "w")
n = text_file.write(Envstring)
text_file.close()


##########################
#Membrane

MemMut = pd.read_csv('./Envelope Mutation F.fasta', sep='\t')

Memstring = " "


MemMut_location = MemMut.iloc[:,0]

count = 0 
for row in MemMut_location:
    for value in row:
        count += 1
        if 26523 <= count >= 27191:
            Memstring = Memstring + value + " "

#reference
#https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
def remove(string): 
    return string.replace(" ", "")
                      

Memstring = remove(Memstring)

count = 0
for i in Memstring:
    count += 1

#print(count)

text_file = open("Mem_M_from_python.txt", "w")
n = text_file.write(Memstring)
text_file.close()





    

