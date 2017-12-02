"""
title: convert fasta alignment to phylip format for PAML
author: Bin He
date: 1 dec 2017
"""

from glob import glob
from Bio import AlignIO

# list all files
all_files = glob("../data/alignment/coding/*.codon.mfa")
f = all_files[0]

aln = AlignIO.read(f, "fasta")
L = aln.get_alignment_length()
aln = aln[:, 0:L-3] # to remove the last three nucleotides (stop codon)

# edit the sequence name to retain only the species name part
for record in aln:
    record.id = record.id.split("_")[0]

AlignIO.write(aln, "test.phy", "phylip-sequential")
