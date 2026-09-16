#! /usr/bin/env python

import sys

#DNASeq = input("Enter DNA sequence: ")
DNASeq = sys.argv[1]
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ", "")

print("\n"+DNASeq+"\n")

SeqLength = len(DNASeq)

print("Sequence Length: "+str(SeqLength))

NumberA = DNASeq.count("A")

NumberC = DNASeq.count("C")

NumberG = DNASeq.count("G")

NumberT = DNASeq.count("T")

print("A: ", f'{NumberA/SeqLength:.2f}')
print("C: ", f'{NumberC/SeqLength:.2f}')
print("G: ", f'{NumberG/SeqLength:.2f}')
print("T: ", f'{NumberT/SeqLength:.2f}')

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT
if SeqLength >= 14:
	MeltTempLong = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	print("\nTm Long (>14): " + f'{MeltTempLong:.4f}' + " C\n")

else:
	MeltTempShort = (4 * TotalStrong) + (2 * TotalWeak)
	print("\nTm Short (<14): " + f'{MeltTempShort:.4f}' + " C\n")

BaseList = "ATCG"

for Base in Baselist:
	Percent = 100 * DNASeq.count(Base) / SeqLength
	#print(Base+ " "+str(Percent))
	print("%s: %4.1f" % (Base, Percent))

