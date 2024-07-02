# scRNAseqStatsBook
## Description scRNAseqReportGen is a Python package designed to streamline the analysis and reporting of single-cell RNA sequencing (scRNA-seq) data. This package provides a user-friendly and automated way to generate comprehensive LaTeX reports from scRNA-seq matrix data, including detailed distributions and basic statistics for each gene.
## Key Features
- **Automated Report Generation**: Easily create LaTeX-formatted reports with minimal manual intervention.
- **Statistical Analysis**: Compute and display basic statistics such as mean, median, zero count, and non-zero count for each gene.
- **Visual Representations**: Generate histograms to visually represent the distribution of gene expression data.
- **LaTeX Integration**: Seamlessly integrate statistical tables and plots into a structured LaTeX document.
- **PDF Compilation**: Automatically compile the LaTeX document into a PDF, providing a ready-to-share report.

## Functionality
The core functionality of scRNAseqReportGen revolves around processing scRNA-seq data stored in CSV files and generating a LaTeX document with the following components for each gene:

- **Gene Distribution Plots**: Histograms displaying the distribution of gene expression values.
- **Statistical Tables**: Tables summarizing key statistics such as mean, median, zero count, and non-zero count.
- **Sectioned Reports**: Organized sections and subsections in the LaTeX document for easy navigation and readability.

## Installation
```bash
pip install scRNAseqStatsBook

## Usage
import scRNAseqStatsBook
scRNAseqStatsBook.generate_report('path_to_your_csv_files')

