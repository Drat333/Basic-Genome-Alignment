##Implementation of Hirschberg's Algorithm by Adrian Zugaj
##Linear space implementation of NW
import nw

def NWScore(seq1,seq2,m,mm,g):
    
    Score = []
    row = [0]
    for j in range(1,len(seq2)):
        row.append(row[j-1] + g)
    Score.append(row)
    row = []
    #print Score
    for i in range(1,len(seq1)):      #i is rows
        row = [Score[i-1][0] + g]
        for j in range(1,len(seq2)):
            if seq1[i] == seq2[j]:
                scoreD = Score[i-1][j-1] + m
            else:
                scoreD = Score[i-1][j-1] + mm
            scoreU = Score[i-1][j] + g
            scoreL = row[j-1] + g
            row.append(max(scoreD,scoreU,scoreL))
        Score.append(row)
        if i > 1:
            Score[i-2] = []
    
    LastLine = Score[len(seq1)-1]
    return LastLine


def Hirschberg(seq1,seq2,m,mm,g):
    aln1 = ""
    aln2 = ""
    if len(seq1) == 0:
        for i in range(0,len(seq2)):
            aln1 = aln1 + "-"
            aln2 = aln2 + seq2[i]
    elif len(seq2) == 0:
        for i in range(0,len(seq1)):
            aln1 = aln1 + seq1[i]
            aln2 = aln2 + "-"
    elif len(seq1) == 1 or len(seq2) == 1:
        aln1,aln2 = nw.NWAlignment(seq1,seq2,m,mm,g)
    else:
        seq1Len = len(seq1)
        seq1Mid = (len(seq1)/2)
        seq2Len = len(seq2)
        
        scoreL = NWScore(seq1[0:seq1Mid], seq2,m,mm,g)
        scoreR = NWScore(seq1[seq1Mid:seq1Len][::-1], seq2[::-1],m,mm,g)
        seq2Mid = PartitionSeq2(scoreL,scoreR)
        
        hirA1,hirA2 = Hirschberg(seq1[0:seq1Mid],seq2[0:seq2Mid],m,mm,g)
        hirB1,hirB2 = Hirschberg(seq1[seq1Mid:seq1Len],seq2[seq2Mid:seq2Len],m,mm,g)
        aln1 = hirA1 + hirB1
        aln2 = hirA2 + hirB2
    return aln1,aln2
    
def PartitionSeq2(ScoreL,ScoreR):
    ScoreR.reverse()
    Scores = ScoreL + ScoreR  
    return Scores.index(max(Scores))
    
    
    
    
