import pandas as pd
from pathlib import Path
import numpy as np

from src.statistical_tools.common_functions import compute_temporal_std, compute_temporal_average
from src.xls_reader.xls_reader import get_variable_names, get_number_of_variables, get_number_of_probes, \
    get_probe_position, get_number_of_edges, get_edge_names, get_variable_units, create_results_dictionary, \
    check_time_column

##caminho_arquivo_excel = r'C:\Users\Gustavo\OneDrive\Documentos\Engenharia Mecânica - UFSC\Iniciação Cientica - SINMEC\simulacao_caso_tese_dalla_maria.data\dalla_maria_49cases_report.xls'
main_folder = Path(r'C:\Users\Gustavo\OneDrive\Documentos\Engenharia Mecânica - UFSC\Iniciação Cientica - SINMEC\simulacao_caso_tese_dalla_maria.data')
xls_file = Path(main_folder,"dalla_maria_49cases_report.xls")
xls_abas = pd.ExcelFile( xls_file)
sheets = xls_abas.sheet_names
for sheet in range (4):
    dataframe = pd.read_excel(xls_file , sheet_name= sheets[sheet])
    result_dictionary = create_results_dictionary(dataframe)



a=2
# dataframe = [None]*2
# for sheet in range (2):
#     dataframe[sheet] = pd.read_excel(xls_file , sheet_name= sheets[sheet])
# variables_name =[None]*2
# number_of_variables = [None]*2
# number_of_probes = [None]*2
# probes_position = [None]*2
# number_of_edges = [None]*2
# edges_name = [None]*2
# variable_units = [None]*2
# results_dictionary = [None]*2
# time_values = [None]*2
#
# for i in range (len(dataframe)):
#     variables_name[i] = get_variable_names(dataframe[i])
#     number_of_variables[i] = get_number_of_variables(dataframe[i])
#     number_of_probes[i] = get_number_of_probes(dataframe[i])
#     probes_position[i] = get_probe_position(dataframe[i])
#     number_of_edges[i] = get_number_of_edges(dataframe[i])
#     edges_name[i] = get_edge_names(dataframe[i])
#     variable_units[i] = get_variable_units(dataframe[i])
#     results_dictionary[i] = create_results_dictionary(dataframe[i])
#     time_values[i] = check_time_column(dataframe[i])
# std_value = [[[None]*int(number_of_variables[i])]*int(number_of_probes[i])]*int(number_of_edges[i])
#
# for i in range(len(dataframe)):
#     result_dictionary = results_dictionary[i]
#     for j in range(len(number_of_edges)):
#         edge_name = edges_name[0][j]
#         for k in range (len(number_of_probes)):
#             probe_position = probes_position[0][k]
#             for m in range(len(number_of_variables)):
#                 variable_name = variables_name[0][m]
#
# std_value [0] = compute_temporal_std(time_values[i],result_dictionary['Conn 1']['13.12']['Water Volumetric Flow Rate']['values'])

a=3