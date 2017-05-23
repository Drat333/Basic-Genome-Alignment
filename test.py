import otherHirschberg as hir
import nw
seq1 = "AAAA"
seq2 = "CCAAAATT"

out1,out2 = hir.HirschbergAlign(seq1,seq2,5,1,-2)
print "\nHirschberg:"
print out1
print out2

print "\nNeedleman-Wunsch:"
out1,out2 = nw.NWAlignment(seq1,seq2,5,1,-2)
print out1
print out2
#ACTAGCCAAGTTATAC
#ACTAGCCAAGTTATAC