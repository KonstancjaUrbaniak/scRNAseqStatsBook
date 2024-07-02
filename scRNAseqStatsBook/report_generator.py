import datetime
from pylatex import Document, Section, Command, NewPage, NoEscape, Tabular, Table, Center
import matplotlib.pyplot as plt
import os
import pandas as pd
import subprocess
import re

def create_histograms(data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for column in data.columns:
        plt.figure()
        data[column].plot(kind='hist', bins=30, edgecolor='black')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plot_path = os.path.join(output_dir, f'test_report_{column}.png')
        plt.savefig(plot_path)
        plt.close()
        print(f"Saved histogram to: {plot_path}")  # Debugging line
        if not os.path.exists(plot_path):
            print(f"Error: Histogram file {plot_path} was not created.")

def calculate_statistics(data):
    stats = {}
    for column in data.columns:
        col_data = data[column]
        stats[column] = {
            'zeros': (col_data == 0).sum(),
            'non_zeros': (col_data != 0).sum(),
            'mean': col_data.mean(),
            'median': col_data.median(),
            'std': col_data.std(),
            'max': col_data.max(),
            'min': col_data.min()
        }
    return stats

def create_statistics_table(stats, column):
    """Create a LaTeX table for the statistics."""
    table = Table(position='h!')
    with table.create(Center()) as centered_table:
        with centered_table.create(Tabular('l c')) as tabular:
            tabular.add_hline()
            tabular.add_row((NoEscape(r'\textbf{Statistical Measure}'), NoEscape(r'\textbf{Value}')))
            tabular.add_hline()
            tabular.add_row(('Mean', f'{stats[column]["mean"]:.2f}'))
            tabular.add_hline()
            tabular.add_row(('Median', f'{stats[column]["median"]:.2f}'))
            tabular.add_hline()
            tabular.add_row(('Standard Deviation', f'{stats[column]["std"]:.2f}'))
            tabular.add_hline()
            tabular.add_row(('Max', f'{stats[column]["max"]:.2f}'))
            tabular.add_hline()
            tabular.add_row(('Min', f'{stats[column]["min"]:.2f}'))
            tabular.add_hline()
            tabular.add_row(('Number of zeros', f'{stats[column]["zeros"]}'))
            tabular.add_hline()
            tabular.add_row(('Number of non-zeros', f'{stats[column]["non_zeros"]}'))
            tabular.add_hline()
    return table

def create_latex_report(data, filename, output_dir, author):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    doc = Document(documentclass='article', document_options='a4paper')
    doc.packages.append(Command('usepackage', 'placeins'))  # Include placeins package
    doc.packages.append(Command('usepackage', 'graphicx'))  # Include graphicx package
    author = author 
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    create_cover_page(doc, f"Report for: {filename}", author, current_date)

    doc.append(NewPage())

    stats = calculate_statistics(data)
    create_histograms(data, output_dir)

    for column in data.columns:
        with doc.create(Section(f'Statistics for {column}')):
            image_filename = os.path.abspath(os.path.join(output_dir, f'test_report_{column}.png'))
            if os.path.exists(image_filename):
                print(f"Adding image to LaTeX document: {image_filename}")
                doc.append(NoEscape(r'\begin{figure}[h!]'))
                doc.append(NoEscape(r'\centering'))
                doc.append(NoEscape(r'\includegraphics[width=\textwidth]{' + image_filename.replace('_', r'\_') + '}'))
                doc.append(NoEscape(r'\caption{Distribution of ' + column + '}'))
                doc.append(NoEscape(r'\end{figure}'))

            doc.append(NoEscape(r'\begin{center}'))
            doc.append(NoEscape(r'\textbf{Statistics for ' + column + '}'))
            doc.append(NoEscape(r'\end{center}'))
            table = create_statistics_table(stats, column)
            doc.append(table)
            doc.append(NewPage())

    tex_filename = os.path.join(output_dir, f'{filename}.tex')
    doc.generate_tex(tex_filename[:-4])  # Remove the .tex extension before passing to generate_tex
    compile_latex_document(output_dir, f'{filename}.tex')

def create_cover_page(doc, title, author, date):
    doc.preamble.append(Command('title', NoEscape(r'\huge ' + NoEscape.escape_latex(title))))
    doc.preamble.append(Command('author', NoEscape(r'\Large ' + NoEscape.escape_latex(author))))
    doc.preamble.append(Command('date', NoEscape(r'\Large ' + NoEscape.escape_latex(date))))
    doc.append(NoEscape(r'\maketitle'))

def compile_latex_document(output_dir, tex_filename):
    command = ['pdflatex', tex_filename]
    print(f"Running command: {command} in directory: {output_dir}")
    result = subprocess.run(command, check=True, cwd=output_dir)
    print(result.stdout)
    print(result.stderr)

# Correct escape method for NoEscape
class NoEscape(NoEscape):
    @staticmethod
    def escape_latex(text):
        """
        Escape LaTeX special characters in text.
        """
        conv = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\textasciicircum{}',
            '\\': r'\textbackslash{}',
        }
        regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key=lambda item: - len(item))))
        return regex.sub(lambda match: conv[match.group()], text)
