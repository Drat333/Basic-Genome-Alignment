import genomealignment
import time

file = open("output-20160513-182147.fasta", "r")
input = file.readlines()
file.close()

genome1 = input[1].rstrip("\n")
genome2 = input[3].rstrip("\n")
kmer = 10

#genome1 = "GATATAGGTATAGGGAGCGATACACGAT"
#genome2 = "GACACCTATACATAGCGATACGAT"
#kmer = 4

print "\nAligning genomes:"
print input[0].lstrip(">").rstrip("\n")
print input[2].lstrip(">")

#(aln1, aln2) = genomealignment.genomeAlignment(genome1, genome2, kmer)
aln1 = genome1.upper()
aln2 = genome2.upper()

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "output-20160513-182147-UPPER.fasta"
file = open(filename, "w")
file.write(input[0])
file.write(aln1+"\n")
file.write(input[2])
file.write(aln2+"\n")
file.close()

print "Saved alignment to " + filename