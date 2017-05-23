from __future__ import print_function
from Hirschberg import HirschbergAlign as align
import longestIncreasingSubsequence
from collections import defaultdict

def genomeAlignment(genome1, genome2, k):
    
    ##Needleman-Wunsch values
    m = 5
    mm = -4
    g = -26

    ##initialize dictionaries for genome region match indexes
    listKmerIndex   = []        ##contains indices for kmers in both genomes. Once sorted, index of this array is also the kmer number
    dictKmerSeq     = {}        ##key = kmer number, value = kmer string
    
    
    
    
    ####Build kmer dictionaries and compare them####

    print("k-length =", k)
    ##build dictionary of kmers for genome 1
    print("Building genome1 kmer dictionary...")
    dictGenome1 = defaultdict(list)
    i = 0
    for i in range(len(genome1) - k + 1):
        seq = genome1[i:i+k]
        dictGenome1[seq].append(i)
        
    ##build dictionary of kmers for genome 2
    print("Building genome2 kmer dictionary...")
    dictGenome2 = defaultdict(list)
    i = 0
    for i in range(len(genome2) - k + 1):
        seq = genome2[i:i+k]
        dictGenome2[seq].append(i)
    
    ##compare kmers between genomes
    print("Comparing kmers...")
    for kmer in (dictGenome1.keys()):
        if kmer in dictGenome2:
            minDiff = float("inf")
            for index1 in (dictGenome1[kmer]):
                for index2 in (dictGenome2[kmer]):
                    diff = abs(index1 - index2)
                    if diff < minDiff:
                        minDiff = diff
                        (x,y) = index1,index2

            listKmerIndex.append((x,y))
    #unload kmer dictionaries
    dictGenome1 = {}
    dictGenome2 = {}
    listKmerIndex.append((len(genome1),len(genome2)))
    listKmerIndex = sorted(listKmerIndex)               #sort by genome1 indices
    dictGen2Indices = {}
    i = 0
    for i in range(len(listKmerIndex)):
        dictKmerSeq[i] = genome1[listKmerIndex[i][0]:listKmerIndex[i][0] + k]
        dictGen2Indices[listKmerIndex[i][1]] = i
    
    
    ####Get longest increasing subsequence of k matches and removes kmer collisions
    listGen2Indices = sorted(dictGen2Indices.keys())
    
    ##gets longest increasing subsequence
    print("Getting longest increasing subsequence of kmers...")
    order = []                              #contains order of kmer numbers
    for key in listGen2Indices:             
        order.append(dictGen2Indices[key])  #keys are genome 2 indices, values are associated kmer numbers
        
    order = longestIncreasingSubsequence.longest_increasing_subsequence(order)

    ##removes collisions in genome1 indices
    print("Removing kmer collisions...")
    i = 0
    while i < (len(order) - 2):
        if (listKmerIndex[order[i+1]][0]-listKmerIndex[order[i]][0]) < k:
            while (listKmerIndex[order[i+1]][0]-listKmerIndex[order[i]][0] < k) and (i + 1 < len(order) - 1):
                del order[i+1]
        i += 1
    
    ##removes collisions in genome2 indices
    i = 0
    while i < (len(order) - 2):
        if (listKmerIndex[order[i+1]][1]-listKmerIndex[order[i]][1]) < k:
            while (listKmerIndex[order[i+1]][1]-listKmerIndex[order[i]][1] < k) and (i + 1 < len(order) - 1):
                del order[i+1]
        i += 1
    
    ##save memory
    listGenomeSeq = []
    index1 = listKmerIndex[order[0]][0]
    index2 = listKmerIndex[order[0]][1]
    listGenomeSeq.append((genome1[0:index1], genome2[0:index2]))
    i = 0
    for i in range(len(order) - 2):
        index1start  = listKmerIndex[order[i]][0]+k
        index1end    = listKmerIndex[order[i+1]][0]
        index2start  = listKmerIndex[order[i]][1]+k
        index2end    = listKmerIndex[order[i+1]][1]
        listGenomeSeq.append((genome1[index1start:index1end],genome2[index2start:index2end]))
    i+=1
    index1start  = listKmerIndex[order[i]][0]+k
    index2start  = listKmerIndex[order[i]][1]+k
    listGenomeSeq.append((genome1[index1start:],genome2[index2start:]))
    listGenomeSeq.reverse()
    genome1 = ""
    genome2 = ""
    
    
    
    
    ####Create complete alignment using alternating NW and k matches####
    
    aln1 = []
    aln2 = []
    length = len(order) - 1
    print("\nAligning with", length, "kmers.")
    print("Generating alignment...\n")
    
    ##NW align from genomes start to first kmer
    percentage = 0
    progress = "\r%.5f%% done" % (percentage,)
    print(progress, end='')
    nw1,nw2 = align(listGenomeSeq[-1][0], listGenomeSeq[-1][1], m, mm, g)
    del listGenomeSeq[-1]
    aln1.append(nw1)
    aln2.append(nw2)
    
    i = 0
    for i in range(len(order) - 1):
        percentage = float(i)/length*100
        progress = "\r%.5f%% done" % (percentage,)
        print(progress, end='')
        #print "Starting a NW alignment..."
        ##append matched kmer regions
        aln1.append(dictKmerSeq[order[i]].lower())
        aln2.append(dictKmerSeq[order[i]].lower())
        del dictKmerSeq[order[i]]
        
        ##align non-matched regions using NW
        nw1,nw2 = align(listGenomeSeq[-1][0], listGenomeSeq[-1][1], m, mm, g)
        del listGenomeSeq[-1]
        
        ##append NW aligned regions
        aln1.append(nw1)
        aln2.append(nw2)

    percentage = 100
    progress = "\r%.5f%% done\n" % (percentage,)
    print(progress, end='')
    
    
    
    print("\nGenome alignment completed.")
    aln1 = "".join(aln1)
    aln2 = "".join(aln2)
    return aln1, aln2
