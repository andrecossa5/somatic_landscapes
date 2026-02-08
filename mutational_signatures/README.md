# Mutational Signatures in Cancer Genomics

## Background

### What are Mutational Signatures?

Mutational signatures are characteristic patterns of somatic mutations found in cancer genomes that reflect the underlying mutational processes operating during tumor development. Each signature represents the "molecular fingerprint" left by specific DNA damage and repair mechanisms, environmental exposures, or enzymatic activities that have shaped the cancer genome over time¹.

Rather than being random, cancer genomes display organized patterns of mutations that can be mathematically decomposed into distinct signatures. Each signature is typically characterized by:
- **Trinucleotide context**: The pattern of mutations considering the bases immediately 5' and 3' to the mutated site
- **Mutation types**: The six types of base substitutions (C>A, C>G, C>T, G>A, G>T, T>A) and their reverse complements
- **Relative frequencies**: The proportion of each mutation type within each trinucleotide context

### Types of Mutational Signatures

Mutational signatures can be broadly classified based on their underlying causes:

#### 1. **Endogenous Processes**
- **DNA repair deficiencies**: Signatures associated with defective mismatch repair (MMR), homologous recombination deficiency (HRD), base excision repair, or nucleotide excision repair
- **DNA polymerase errors**: Signatures from replicative polymerase epsilon (POLE) and delta (POLD1) exonuclease deficiencies
- **Spontaneous deamination**: Age-related signatures from cytosine deamination processes

#### 2. **Exogenous Exposures**
- **Environmental carcinogens**: UV radiation, tobacco smoking, aristolochic acid exposure
- **Medical treatments**: Chemotherapy agents (alkylating agents, platinum compounds), radiation therapy
- **Infectious agents**: Hepatitis B virus, human papillomavirus, Helicobacter pylori

#### 3. **Unknown Etiology**
- Several signatures have been identified through computational methods but lack clear biological explanations, representing areas of active research¹.

### Analysis Pipeline

The typical mutational signature analysis workflow consists of two main approaches:

#### 1. **De Novo Signature Extraction**
This approach identifies new signatures directly from the data without prior knowledge:
- **Input**: Mutation catalogs from multiple samples (typically >100 samples)
- **Method**: Matrix factorization techniques (e.g., Non-negative Matrix Factorization, NMF)
- **Output**: New signature profiles and their activities across samples
- **Use case**: Discovery of novel signatures in new datasets or cancer types

#### 2. **Signature Assignment/Fitting**
This approach quantifies the contribution of known signatures in individual samples:
- **Input**: Mutation catalog from single or multiple samples + reference signature database (e.g., COSMIC signatures)
- **Method**: Optimization algorithms that fit known signatures to observed mutations
- **Output**: Activity levels of each signature in each sample
- **Use case**: Clinical applications and mechanistic understanding of individual tumors

### Computational Methods

#### **Matrix Factorization Approaches**
- **SigProfilerExtractor**: Uses NMF with stability and statistical testing
- **[MutationalPatterns](https://github.com/ToolsVanBox/MutationalPatterns)**: R/Bioconductor package for extracting and visualizing mutational patterns in SNVs, indels, DBSs, and MBSs⁵
- **[signeR](https://bioconductor.org/packages/release/bioc/html/signeR.html)**: Empirical Bayesian approach to mutational signature discovery with automatic signature number determination⁶
- **[HDP](https://github.com/nicolaroberts/hdp)**: R package implementing Hierarchical Dirichlet Process for modeling categorical count data with automatic determination of signature numbers

#### **Assignment Methods**
- **SigProfilerAssignment**: Probabilistic assignment of signatures to samples and individual mutations⁴
- **MutationalPatterns fitting**: Least-squares optimization for signature fitting (part of [MutationalPatterns](https://github.com/ToolsVanBox/MutationalPatterns) package)
- **sigfit**: Flexible Bayesian framework for signature analysis
- **[MuSiCal](https://github.com/parklab/MuSiCal)**: Comprehensive toolkit combining minimum-volume NMF (mvNMF) for de novo discovery with likelihood-based sparse NNLS for signature matching and refitting

#### **Machine Learning Approaches**
Recent developments include deep learning methods and more sophisticated statistical frameworks that can handle:
- **Temporal dynamics**: How signatures change over tumor evolution²
- **Uncertainty quantification**: Providing confidence intervals for signature activities
- **Multi-scale analysis**: Integrating signatures across different genomic scales

A comprehensive evaluation of twelve different tools for fitting mutational signatures has shown significant performance differences across cancer types and data characteristics³.

### Importance in Cancer Research

#### **Mechanistic Understanding**
Mutational signatures provide insights into:
- **Cancer etiology**: Identifying causative factors in cancer development
- **DNA repair mechanisms**: Understanding how repair deficiencies contribute to tumorigenesis
- **Tumor evolution**: Tracking how mutational processes change during cancer progression

#### **Clinical Applications**
- **Precision medicine**: Identifying patients likely to respond to specific therapies (e.g., PARP inhibitors for HRD tumors, immunotherapy for MMR-deficient cancers)
- **Risk assessment**: Quantifying cancer risk from environmental exposures
- **Treatment monitoring**: Tracking therapy-induced mutational changes
- **Biomarker development**: Using signature patterns as diagnostic or prognostic markers

### Signatures in Normal Tissues

Recent research has revealed that mutational signatures are not exclusive to cancer:
- **Aging signatures**: Normal tissues accumulate specific mutational patterns with age
- **Environmental exposure**: Healthy tissues from exposed individuals (e.g., smokers) show exposure-related signatures
- **Stem cell dynamics**: Different signatures operate in various normal tissue compartments
- **Early detection**: Understanding baseline mutational patterns may help identify pre-cancerous changes³

This expanding understanding suggests that mutational signatures represent fundamental biological processes operating throughout life, with cancer representing an extreme manifestation of these underlying mechanisms.

## Course Structure

### Task #1: Introduction to Mutational Signatures with MuSiCal
**Objective**: Provide hands-on introduction to mutational signature concepts and basic analysis

**Content**:
- Interactive exploration using the [intro_mut_signatures.ipynb](intro_mut_signatures.ipynb) notebook
- Introduction to MuSiCal (Mutational Signature Calculator) tool
- Understanding trinucleotide contexts and signature visualization
- Basic signature extraction and interpretation
- Practical exercises with simulated data

**Learning Outcomes**:
- Understand the biological basis of mutational signatures
- Interpret signature plots and profiles
- Perform basic signature analysis using computational tools
- Recognize common signature patterns and their biological meanings

### Task #2: Exploring Mutational Signatures in PCAWG Data
**Objective**: Apply MuSiCal to real pan-cancer genomic data
**Content**:
- Analysis of Pan-Cancer Analysis of Whole Genomes (PCAWG) dataset
- Comparative signatures across cancer types
- Investigation of signature co-occurrence patterns
- Interpret signatures as mutagenic exposures or endogenous processes (see [COSMIC](https://cancer.sanger.ac.uk/signatures/sbs))

**Data**: 
- PCAWG signature profiles ([data/PCAWG-146_profiles.csv](data/PCAWG-146_profiles.csv))
- Comprehensive mutation catalogs from >2,600 cancer samples

**Learning Outcomes**:
- Compare signature patterns across different cancer types
- Identify clinically relevant signature associations
- Develop skills in data interpretation and hypothesis generation

## Getting started

This session will go through:

- `intro_mut_sigantures.ipynb` - Comprehensive tutorial with simulated data
- `pcawg_analysis.ipynb` - Mutational signatures exercise 

### Prerequisites
- Basic understanding of molecular biology and cancer genetics
- Familiarity with python programming (advantageous)
- Knowledge of genomics concepts (mutations, selection, etc)

### Software Requirements
- mamba
- VSCode
- jupyter notebook

### Setting up the environment
Easy one. We will create and activate a `conda` environment with `mamba`.

First (if not done already) install `mamba`:

```
wget https://github.com/conda-forge/miniforge/releases/download/25.11.0-1/Miniforge3-25.11.0-1-MacOSX-arm64.sh
zsh Miniforge3-25.11.0-1-MacOSX-arm64.sh -b -p /mambaforge3
```

Open another terminal, ensure `mamba` is correctly installed:

```
mamba -h
```

Navigate to the path to your cloned `somatic_landscapes` github repo. Then:

```
cd mutational_signatures/envs
mamba env create -f signatures.yml -n musical
mamba activate musical
```

Ensure you have a functional environment by firing up the `python` interpreter, and then assessing:

```python
import musical
musical.__version__
```

NB: **make sure** you have chosen this environment when opening the notebooks in VSCode or jupyter.


## References

1. Genomics Education Programme, NHS England. "Mutational Signatures." https://www.genomicseducation.hee.nhs.uk/genotes/knowledge-hub/mutational-signatures/

2. Alexandrov, L.B., et al. "The repertoire of mutational signatures in human cancer." *Nature Reviews Cancer*, 2021. https://www.nature.com/articles/s41568-021-00377-7

3. Medo, M., Ng, C.K.Y., Medová, M. "A comprehensive comparison of tools for fitting mutational signatures." *Nature Communications*, 2024. https://doi.org/10.1038/s41467-024-53711-6

4. Díaz-Gay, M., Vangara, R., Barnes, M., et al. "Assigning mutational signatures to individual samples and individual somatic mutations with SigProfilerAssignment." *Bioinformatics*, 2023.

5. Manders, F., Brandsma, A.M., de Kanter, J., et al. "MutationalPatterns: the one stop shop for the analysis of mutational processes." *BMC Genomics*, 2022. https://doi.org/10.1186/s12864-022-08357-3

6. Rosales, R.A., Drummond, R.D., Valieris, R., et al. "signeR: An empirical Bayesian approach to mutational signature discovery." *Bioinformatics*, 2017. https://doi.org/10.1093/bioinformatics/btw572

---

*This course material is designed for wet lab scientists transitioning into computational cancer genomics.*