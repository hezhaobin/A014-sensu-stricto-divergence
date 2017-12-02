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
def myPAML( f, format="fasta" ):
    """ Use PAML to estimate syn and nonsyn divergence
    Args:
        f (str): the path and filename
        format (str): format of the input alignment, e.g. "fasta"
    Returns:
        parsed output from PAML
    """
    aln = AlignIO.read(f, format)
    L = aln.get_alignment_length()
    """ 
    to remove the last three nucleotides (stop codon)
    changed to remove the last 6 because some sequences
    have misaligned stop codons that appear in the second
    to last codon position
    """

    aln = aln[:, 0:L-6] 
    
    # edit the sequence name to retain only the species name part
    for record in aln:
        record.id = record.id.split("_")[0]
    
    AlignIO.write(aln, "./scratch/tmp.phy", "phylip-sequential")

    # initialize the PAML codeml object
    cml = codeml.Codeml()
    cml.working_dir = "./scratch"
    cml.alignment = "./scratch/tmp.phy"
    cml.tree = "./scratch/tree"
    cml.read_ctl_file("./scratch/codonml.ctl")
    cml.out_file = "./scratch/" + f.split("_")[1] + ".mlc" # name the output file

    # run PAML
    # note that the working_dir take effect for ctl_file, but not the others
    result = cml.run()

    return result;

    
# open file for output
OUT = open("../output/2017-12-01-Scer-Spar.txt", "w")

# list all files
all_files = glob("../data/alignment/coding/*.codon.mfa")
print( "There are %i files" % len(all_files) )

i = 0 # counter

for IN in all_files:
    # get gene name
    gene = IN.split("_")[1]
    # run PAML
    result = myPAML(IN, "fasta")
    dist = result['pairwise']['Scer']['Spar']
    value = [dist[x] for x in ['dN','dS','omega']]
    OUT.write( "\t".join([gene]+map(str, value)) + "\n" )
    # progress report
    i = i + 1
    if i % 100 == 0:
        print( i )
