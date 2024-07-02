import os
import pandas as pd
from scRNAseqStatsBook.report_generator import create_latex_report

def test_create_latex_report():
    file_path = 'tests/genesSetTest.csv'
    data = pd.read_csv(file_path)
    output_dir = 'tests/output'
    os.makedirs(output_dir, exist_ok=True)
    create_latex_report(data, 'test_report', output_dir,'Konstancja Urbaniak')