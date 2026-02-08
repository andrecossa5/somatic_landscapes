# EMBO Nextflow Course 2026: somatic Landascapes

## Overview

This course focuses on the **characterization of somatic landscapes** - the mutations acquired during individual lifespan and how these mutations impact cell and tissue phenotypes. The course is structured around two complementary analytical modules that together provide a comprehensive understanding of somatic evolution.

## Course Modules

### Module 1: Mutational Signatures ([mutational_signatures/](mutational_signatures/))

This module explores the **molecular fingerprints** left by different mutational processes in cancer genomes. Mutational signatures reveal characteristic patterns of DNA damage from endogenous processes (DNA repair deficiencies, aging), exogenous exposures (UV, smoking, chemotherapy), and unknown etiologies.

**Task 1:** Introduction to Mutational Signatures with MuSiCal
- Interactive exploration using [intro_mut_signatures.ipynb](mutational_signatures/intro_mut_signatures.ipynb)
- Understanding trinucleotide contexts and signature visualization
- Basic signature extraction and interpretation with simulated data

**Task 2:** Exploring Mutational Signatures in PCAWG Data  
- Analysis of real pan-cancer genomic data using [pcawg_analysis.ipynb](mutational_signatures/pcawg_analysis.ipynb)
- Comparative signatures across cancer types using PCAWG dataset
- Investigation of signature co-occurrence patterns and clinical relevance

### Module 2: Selection Analysis ([selection/](selection/))

This module focuses on distinguishing **driver mutations** that provide selective advantages from neutral "passenger" mutations. Using dN/dS statistical methods, it identifies genes under positive selection that fuel tumor progression and represent early molecular events in cancer development.

**Task 1:** Tutorial - dN/dS Analysis of Cancer Data
- Learn fundamentals using [dNdScv_tutorial.Rmd](selection/dNdScv_tutorial.Rmd)
- Master the dNdScv statistical framework with simulated breast cancer data  
- Interpret gene-level selection results and create visualizations

**Task 2:** Exercise - Selection in Normal Tissues
- Apply knowledge using [dNdScv_exercise.Rmd](selection/dNdScv_exercise.Rmd)
- Compare selection patterns between normal skin and oesophagus tissues
- Discover tissue-specific patterns of somatic evolution

## Learning Outcomes

By completing this course, participants will:

- **Understand mutational processes**: Master the biological basis and computational analysis of mutational signatures
- **Identify driver mutations**: Use statistical methods to distinguish functional drivers from neutral passengers
- **Analyze real genomic data**: Work with large-scale cancer genomics datasets (PCAWG)
- **Compare tissue contexts**: Understand how somatic evolution differs between normal and cancerous tissues
- **Apply computational tools**: Gain hands-on experience with state-of-the-art analysis pipelines

## Course Structure

| Module | Tasks | Key Tools | Data Types |
|--------|-------|-----------|------------|
| [Mutational Signatures](mutational_signatures/) | 2 tasks (Intro + PCAWG analysis) | MuSiCal, Jupyter notebooks | Cancer mutation catalogs |
| [Selection Analysis](selection/) | 2 tasks (Tutorial + Exercise) | dNdScv, R/RMarkdown | Normal tissue mutations |

## Getting Started

1. **Prerequisites**: Basic understanding of molecular biology, cancer genetics, and genomics concepts
2. **Software**: Python, R, RStudio, VSCode

## Module Details

For detailed information about each module, including background theory, methodological approaches, and specific learning objectives, refer to the individual module README files:

- [Mutational Signatures Module README](mutational_signatures/README.md)
- [Selection Analysis Module README](selection/README.md)

---

*This course material is designed for wet lab scientists transitioning into computational cancer genomics, providing essential skills for understanding somatic evolution in both normal and cancerous tissues.*
