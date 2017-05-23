def obtainAlignmentFromMatrix(matrix,seq1,seq2):
    x=len(seq1)
    y=len(seq2)
    alignedSeq1=""
    alignedSeq2=""

    while x!=0 or y!=0:
        if matrix[x][y]=="D":
            alignedSeq1=seq1[x-1]+alignedSeq1
            alignedSeq2=seq2[y-1]+alignedSeq2
            x-=1
            y-=1
        elif matrix[x][y]=="L":
            alignedSeq1="-"+alignedSeq1
            alignedSeq2=seq2[y-1]+alignedSeq2
            y-=1
        elif matrix[x][y]=="U":
            alignedSeq1=seq1[x-1]+alignedSeq1
            alignedSeq2="-"+alignedSeq2
            x-=1
    return alignedSeq1,alignedSeq2

def NWScore(seq1, seq2, m, mm, g):

    ##Create first row of V and T
    V=[]
    k=[0]
    T=[]
    l=[""]

    for i in range(1, len(seq2)+1):
        k.append(i*g)
        l.append("L")

    V.append(k)
    T.append(l)

    for y in range(1,len(seq1)+1):
        k=[y*g]
        l=["U"]

        for x in range(1,len(seq2)+1):

            ##output1
            if seq1[y-1]==seq2[x-1]:
                output1=V[y-1][x-1]+m
            else:
                output1=V[y-1][x-1]+mm

            ##output2
            output2=(k[x-1])+g

            ##output3
            output3=V[y-1][x]+g

            #determine which is longest, then append
            if output1 >= output2 and output1 >= output3:
                k.append(output1)
                l.append("D")
            elif output2 >= output1 and output2 >= output3:
                k.append(output2)
                l.append("L")
            elif output3 >= output1 and output3 >= output2:
                k.append(output3)
                l.append("U")
            else:
                print("WTF")
                print(output1,output2,output3)
                print(x,y)

        V.append(k)
        T.append(l)
    score = V[len(seq1)][len(seq2)]

    return score


def NWAlignment(seq1, seq2, m, mm, g):

    ##Create first row of V and T
    V=[]
    k=[0]
    T=[]
    l=[""]

    for i in range(1, len(seq2)+1):
        k.append(i*g)
        l.append("L")

    V.append(k)
    T.append(l)

    for y in range(1,len(seq1)+1):
        k=[y*g]
        l=["U"]

        for x in range(1,len(seq2)+1):

            ##output1
            if seq1[y-1]==seq2[x-1]:
                output1=V[y-1][x-1]+m
            else:
                output1=V[y-1][x-1]+mm

            ##output2
            output2=(k[x-1])+g

            ##output3
            output3=V[y-1][x]+g

            #determine which is longest, then append
            if output1 >= output2 and output1 >= output3:
                k.append(output1)
                l.append("D")
            elif output2 >= output1 and output2 >= output3:
                k.append(output2)
                l.append("L")
            elif output3 >= output1 and output3 >= output2:
                k.append(output3)
                l.append("U")
            else:
                print("WTF")
                print(output1,output2,output3)
                print(x,y)

        V.append(k)
        T.append(l)
    alignedSeq1,alignedSeq2=obtainAlignmentFromMatrix(T, seq1, seq2)

    return alignedSeq1,alignedSeq2

def substringMatch(seq1,seq2):
    score=0
    for i in range(len(seq1)-2):
        subseq1=seq1[i:i+3]
        for j in range(len(seq2)-2):
            subseq2=seq2[j:j+3]
            if (subseq1==subseq2):
                score+=1
    return score
