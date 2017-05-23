##Adrian Zugaj
import random

f=open("dna.fasta")
data=f.readlines()
for i in range(len(data)):
    data[i]=data[i].rstrip("\n")

seq1=data[1]
seq2=data[3]
columns=len(seq2)+1
rows=len(seq1)+1

T=[]
l=[""]

for i in range(1,columns):
    l.append("L")
T.append(l)

for j in range(1,rows):
    l=["U"]
    for i in range(1,columns):
        l.append(random.choice("ULD"))
    T.append(l)

for i in range(rows):
    print(T[i])



##Traceback

alignedSeq1=""
alignedSeq2=""
x=rows-1
y=columns-1
step=0

while x!=0 or y!=0:
    print(x)
    print(y)
    print()
    if T[x][y]=="D":
        alignedSeq1=seq1[x-1]+alignedSeq1
        alignedSeq2=seq2[y-1]+alignedSeq2
        x-=1
        y-=1
    elif T[x][y]=="L":
        alignedSeq1="-"+alignedSeq1
        alignedSeq2=seq2[y-1]+alignedSeq2
        y-=1
    elif T[x][y]=="U":
        alignedSeq1=seq1[x-1]+alignedSeq1
        alignedSeq2="-"+alignedSeq2
        x-=1

print(alignedSeq1)
print(alignedSeq2)

