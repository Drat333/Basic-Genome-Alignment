import genomealignment
import time

file = open("input2.fasta", "r")
input = file.readlines()
file.close()

genome1 = input[1].rstrip("\n")
genome2 = input[3].rstrip("\n")
kmer = 20

#genome1 = "ACTTTTATAAGGATACAGATGCTGTACAGTTCTCGTATCTAC"
#genome2 = "TATAAACCCACAGACAATCGATTTCACTTCTATCGT"
#kmer = 4

print "\nAligning genomes:"
print input[0].lstrip(">").rstrip("\n")
print input[2].lstrip(">")

(aln1, aln2) = genomealignment.genomeAlignment(genome1, genome2, kmer)

timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "output-" + timestr + ".fasta"
file = open(filename, "w")
file.write(input[0])
file.write(aln1+"\n")
file.write(input[2])
file.write(aln2+"\n")
file.close()

print "Saved alignment to " + filename
