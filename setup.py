from setuptools import setup, find_packages

setup(
    name='scRNAseqStatsBook',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'pylatex',
        'subprocess'
    ],
    author='Konstancja Urbaniak',
    author_email='konstancja.urbaniak@gmail.com',
    description='scRNAseqReportGen is a Python package designed to streamline the analysis and reporting of single-cell RNA sequencing (scRNA-seq) data. This package provides a user-friendly and automated way to generate comprehensive LaTeX reports from scRNA-seq matrix data, including detailed distributions and basic statistics for each gene.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KonstancjaUrbaniak/scRNAseqStatsBook',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)