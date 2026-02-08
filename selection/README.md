# Selection Analysis Module

## Overview

Understanding which mutations provide a selective advantage is fundamental to cancer biology and somatic evolution (Martincorena & Campbell 2015). While most somatic mutations are neutral "passengers," a subset are functional "drivers" that promote clonal expansion by conferring growth advantages to cells (Martincorena et al. 2017). Identifying these driver mutations is crucial not only in established cancers, where they fuel tumor progression and therapeutic resistance, but also in normal and precancerous tissues, where they represent the earliest molecular events in cancer development (Alexandrov et al. 2016). The dN/dS method (Kryazhimskiy & Plotkin 2008) quantifies the balance between non-synonymous and synonymous mutations to detect positive selection acting on protein-coding genes, providing a powerful statistical framework to distinguish driver genes from passengers across diverse tissue contexts.

## Course Structure

### Task 1: Tutorial - dN/dS Analysis of Cancer Data
**File:** `dNdScv_tutorial.Rmd`

Learn the fundamentals of dN/dS analysis using the dNdScv method on simulated breast cancer data. This comprehensive tutorial covers:
- Input data requirements and quality control
- Understanding the dNdScv statistical framework
- Interpreting gene-level selection results
- Calculating confidence intervals for effect sizes
- Creating publication-quality visualizations

### Task 2: Exercise - Selection in Normal Tissues
**File:** `dNdScv_exercise.Rmd`

Apply your knowledge to compare selection patterns between normal skin and oesophagus tissues. This comparative analysis explores:
- Interpreting selection signals in normal tissue homeostasis
- Discover tissue-specific patterns of somatic evolution

## Key Learning Outcomes

- Master the dN/dS method for quantifying natural selection in somatic evolution
- Distinguish between neutral passenger and functional driver mutations
- Understand tissue-specific patterns of clonal selection
- Interpret statistical evidence for positive selection in both cancer and normal tissues
- Create effective visualizations for selection analysis results

## Getting started

This session will go through:

- `dNdScv_tutorial.Rmd` - Comprehensive tutorial with breast cancer data
- `dNdScv_exercise.Rmd` - Comparative analysis exercise

### Prerequisites
- Basic understanding of molecular biology and cancer genetics
- Familiarity with R programming (advantageous)
- Knowledge of genomics concepts (mutations, selection, etc)

### Software Requirements
- RStudio

### Setting up the environment
Easy one. Just open `dNdScv_tutorial.Rmd` in `RStudio` and follow the tutorials. Package will be installed as you go.

## References

- [Kryazhimskiy & Plotkin (2008). The population genetics of dN/dS. *PLoS Genetics*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2596312/)
- [Martincorena et al. (2017). Universal Patterns of Selection in Cancer and Somatic Tissues. *Cell*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5720395/)
- [Martincorena & Campbell (2015). Somatic mutation in cancer and normal cells. *Science*](https://www.science.org/doi/full/10.1126/science.aab4082)
- [Alexandrov et al. (2016). Mutational signatures associated with tobacco smoking in human cancer. *Science*](https://www.science.org/doi/full/10.1126/science.aag0299)
- Access required: [Nature article](https://www.nature.com/articles/s41586-025-09792-4)
