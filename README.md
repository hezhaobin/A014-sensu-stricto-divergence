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

### [27 nov 2017] start the analysis

- Downloaded the multiple alignment
- Found Dujon 2006 to contain some useful information
- Talked to Patrick and decided to go with PAML. Will test it tomorrow.
