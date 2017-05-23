##Adrian Zugaj
import random

def obtainSequences(filename):
    f=open(filename)
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].rstrip("\n")

    return data

def randomTracebackMatrix(seq1,seq2):
    columns=len(seq2)+1
    rows=len(seq1)+1

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

    return

def obtainAlignmentFromMatrix(matrix,seq1,seq2):
    x=len(seq1)
    y=len(seq2)
    alignedSeq1=""
    alignedSeq2=""
    
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
    return alignedSeq1,alignedSeq2



##Program Start

data=obtainSequences("dna.fasta")

T=[]
l=[""]
randomTracebackMatrix(data[1],data[2])
alignedSeq1,alignedSeq2=obtainAlignmentFromMatrix(T,data[1],data[3])

print(alignedSeq1)
print(alignedSeq2)

