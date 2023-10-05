from pathlib import Path

import pandas as pd
import pytest
import numpy as np

from src.xls_reader.xls_reader import get_variables_names, get_number_of_variables, get_number_of_probes, \
    get_probe_position, get_number_of_edges, get_edge_names, get_variable_units, \
    create_results_dictionary


@pytest.fixture(scope='session')
def alfasim_file_1():
    main_folder = Path(r"C:\Users\Gustavo\OneDrive\Documentos\Engenharia Mecânica - UFSC\Iniciação Cientica - SINMEC")
    xls_file = Path(main_folder, "multi_transient_reader", "transient_example_short.xlsx")

    return {'dataframe': pd.read_excel(xls_file, decimal=","),
            'variable_names': sorted(['Time', 'Absolute Pressure', 'Holdup']),
            'edge_names': ['Conn 1'],
            'probe_positions': ([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8.0, 8.5, 9, 9.5]),
            'units': sorted(['s', 'bar', 'm3/m3'])}


def test_get_variables_names(alfasim_file_1):
    variable_names = get_variables_names(alfasim_file_1['dataframe'])
    assert variable_names == alfasim_file_1['variable_names']


def test_get_number_of_variables(alfasim_file_1):
    number_single_variables_names = get_number_of_variables(alfasim_file_1['dataframe'])
    assert number_single_variables_names == len(alfasim_file_1['variable_names'])


def test_get_number_of_probes(alfasim_file_1):
    number_of_single_position_probes = get_number_of_probes(alfasim_file_1['dataframe'])
    assert number_of_single_position_probes == len(alfasim_file_1['probe_positions'])


def test_get_probe_position(alfasim_file_1):
    probes_single_position = get_probe_position(alfasim_file_1['dataframe'])
    assert probes_single_position == alfasim_file_1['probe_positions']


def test_get_number_of_edges(alfasim_file_1):
    single_edges_names_number = get_number_of_edges(alfasim_file_1['dataframe'])
    assert single_edges_names_number == len(alfasim_file_1['edge_names'])


def test_get_edge_names(alfasim_file_1):
    single_edges_names = get_edge_names(alfasim_file_1['dataframe'])
    assert single_edges_names == alfasim_file_1['edge_names']


def test_get_variable_units(alfasim_file_1):
    unit_names = get_variable_units(alfasim_file_1['dataframe'])
    assert unit_names == alfasim_file_1['units']


@pytest.mark.skip(reason="change fixture")
def test_create_variables_dictionaries(alfasim_file_1):
    variables_dictionary = create_variables_dictionaries(alfasim_file_1['dataframe'])
    assert variables_dictionary == 1


def test_check_time_column():
    assert "Time"

def test_create_results_dictionary(alfasim_file_1):
    results_dictionary = create_results_dictionary(alfasim_file_1['dataframe'])
    assert results_dictionary == 1

