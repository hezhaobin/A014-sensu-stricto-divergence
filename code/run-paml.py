"""
title: Use PAML to estimate synonymous and nonsynonymous divergence between aligned sequences
author: Bin He
date: 1 dec 2017
"""

# loading requirements
from glob import glob
from Bio import AlignIO
from Bio.Phylo.PAML import codeml

# define functions
def myRead( f, format="fasta" ):
    """ Read the content of an alignment file into an AlignIO object
    Args:
        f (str): the path and filename
        format (str): format of the input alignment, e.g. "fasta"
    Returns:
        PHYLIP-intercleaved format alignment written to "tmp.phy"
    """
    aln = AlignIO.read(f, format)
    L = aln.get_alignment_length()
    aln = aln[:, 0:L-3] # to remove the last three nucleotides (stop codon)
    
    # edit the sequence name to retain only the species name part
    for record in aln:
        record.id = record.id.split("_")[0]
    
    AlignIO.write(aln, "tmp.phy", "phylip-relaxed")
    return;

def myPAML():
    # Run PAML and parse the output

    
# initialize the PAML codeml object
cml = codeml.Codeml()
cml.alignment = "
# list all files
all_files = glob("../data/alignment/coding/*.codon.mfa")
myRead( all_files[0], "fasta" )


