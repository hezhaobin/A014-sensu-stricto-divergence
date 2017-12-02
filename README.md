---
title: estimate coding sequence divergence between _sensu stricto_ species of yeast
author: Bin He
date: 27 nov 2017
---

## Goal

Estimate the level of synonymous and nonsynonymous divergence between _sensu stricto_ species of yeasts. This was motivated by a discussion with Peter Andolfatto. I also wish to know this, namely how distantly related are the yeast species relative to each other.

## Approach

1. The paper that described the genomic sequences of the _sensu stricto_ group is [Scannell et al 2011](http://www.g3journal.org/content/1/1/11). In [Figure 3](http://d2vw8dvx0mg08w.cloudfront.net/content/ggg/1/1/11/F3.large.jpg?width=800&height=600&carousel=1) of that paper, they gave the "relaxed molecular clock estimates of divergence" based on a subset of 106 genes. However, I don't understand what the "substitution per site" stands for and thus unable to directly quote their estimate.

1. Alternatively, I decide to download the multiple alignment from the [website](http://sss.genetics.wisc.edu/cgi-bin/s3.cgi) and use PAML to estimate the level of divergence.

## Notes

### [2 dec 2017] troubleshoot paml in biopython

- Problem
    paml wouldn't run properly, with various errors related to the file path

- Solution
    
    1. I found the Biopython wiki for [PAML](http://biopython.org/wiki/PAML) misleading. In particular, the "working_dir" option is designed to shorten the path of the files as input to paml, e.g. alignment, tree and control. After debugging the code (biopython's), I found that the wrapper function "codeml.py" actually expects absolute paths for those files.
    1. The file format conversion that I got working yesterday produces the "phylip-intercleaved" format. This should work with PAML except that PAML expects a letter "I" on the first line for this format, which the Biopython function left out. I changed the output format to "phylip-sequential" and it worked.

- Notes
    In general, I've found working with Python and Biopython rather enjoyable, due to the ease of reading python code and the fact that the functions for biopython are quite transparent, which means I can debug them without much difficulty.


### [1 dec 2017] apply to many alignment

- Followed [biopython tutorial](https://github.com/peterjc/biopython_workshop/tree/master/reading_writing_alignments) to learn how to use python to read and convert alignment
    - it turned out that the AlignIO module can easily read in an alignment file and write it in PHYLIP format. that's exactly what I need.
    - I can also use split function to modify the sequence name. perfect.
    - also remember to slice the last three columns (stop codon) from the alignment

- Got the code working for 
    1) get the file names for all `*.codon.mfa` in the data directory
    1) read in each file, slice out the last three nucleotides (stop codon) and edit the sequence name to retain only the species names
    1) tested PAML module in biopython, works great

#### Parse the alignment

_Goal_

1. process sequence names to include only 4 letter species abbreviation
1. convert to PHYLIP intercleaved format
1. rename to make it simpler to call in batch mode

### [29 nov 2017] test PAML

- learned about the concepts used in the codon model, such as dS and S*dS, etc.
- tested PAML on one alignment (YBR093C)
    - need to format the alignment file by rewriting the species name
    - used ALIGN to convert the fasta format to PHYLIP (intercleaved)
    - wrote a tree file
    - edited a codonml.ctl
    - stored everything under `analysis/test_paml` folder
- based on this one gene, Scer and Spar are approx ~50% synonymous divergence.
- the next question is how to apply this to a large number of genes and extract the results?

### [27 nov 2017] start the analysis

- Downloaded the multiple alignment
- Found Dujon 2006 to contain some useful information
- Talked to Patrick and decided to go with PAML. Will test it tomorrow.
