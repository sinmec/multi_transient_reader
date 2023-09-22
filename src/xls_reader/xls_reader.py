import pandas as pd
import numpy as np
from pathlib import Path

main_folder = Path(r"C:\Users\Gustavo\OneDrive\Documentos\Engenharia Mecânica - UFSC\Iniciação Cientica - SINMEC")
xls_file = Path(main_folder, "multi_transient_reader", "transient_example.xls")
dataframe = pd.read_excel(xls_file, decimal=",")
column_names = np.array(dataframe.columns.values.tolist()) # Use for read de first cell, the property name, of each column
number_of_lines = dataframe.shape[0]
number_of_columns = dataframe.shape[1]
def get_variables_names(dataframe):
    variables_names = ['Time']
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        variables_names.append(item[:pos_first_open_parentheses-1].strip())
    variables_single_names = set(variables_names)
    return sorted(variables_single_names)
print(get_variables_names(dataframe))
def get_number_of_variables(dataframe):
    variables_names = []
    for item in column_names:
        pos_first_open_parentheses = item.find("(")
        pos_first_open_brackets = item.find("[")
        position = min(pos_first_open_parentheses, pos_first_open_brackets)
        variables_names.append(item[:position - 1].strip())
    number_single_variables = len(set(variables_names))
    return number_single_variables
def get_number_of_probes(dataframe):
    probes_position = []
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        pos_second_open_parentheses = item. find("(",pos_first_open_parentheses+1)
        pos_first_close_parentheses = item.find(")")
        probes_position.append(item[pos_second_open_parenteses:pos_first_close_parentheses+1].strip())
    number_of_single_position_probes = len(set(probes_position))
    return number_of_single_position_probes
def get_probe_location(dataframe):
    probes_position = []
    for item in column_names[1:]:
        pos_first_open_parentheses = item.find("(")
        pos_second_open_parentheses = item.find("(", pos_first_open_parentheses + 1)
        pos_first_close_parentheses = item.find(")")
        probes_position.append(item[pos_second_open_parenteses:pos_first_close_parentheses + 1].strip())
    number_of_single_position_probes = set(probes_position)
    single_position_probes_ordered = sorted(number_of_single_position_probes)
    return single_position_probes_ordered
def get_number_of_edges(dataframe):
    edges_names = []
    for item in column_names[1:]:
        first_open_parentheses = item.find("(")
        second_open_parentheses = item.find("(", first_open_parentheses + 1)
        edges_names.append(item[first_open_parentheses+1:second_open_parentheses-1].strip())
    single_edges_names_number = len(set(edges_names))
    return single_edges_names_number
def get_edge_names(dataframe):
    edges_names = []
    for item in column_names[1:]:
        first_open_parenteses = item.find("(")
        second_open_parenteses = item.find("(", first_open_parenteses + 1)
        edges_names.append(item[first_open_parenteses+1:second_open_parenteses-1].strip())
    single_edges_names = set(edges_names)
    return single_edges_names



